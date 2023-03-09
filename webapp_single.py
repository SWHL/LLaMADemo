import torch
import json

import gradio as gr

from pathlib import Path
from llama import ModelArgs, Transformer, Tokenizer, LLaMA


def load(
    ckpt_dir: str,
    tokenizer_path: str,
    local_rank: int,
    world_size: int,
    max_seq_len: int,
    max_batch_size: int,
) -> LLaMA:
    checkpoints = sorted(Path(ckpt_dir).glob("*.pth"))
    assert world_size == len(
        checkpoints
    ), f"Loading a checkpoint for MP={len(checkpoints)} but world size is {world_size}"
    ckpt_path = checkpoints[local_rank]

    checkpoint = torch.load(ckpt_path, map_location="cpu")

    with open(Path(ckpt_dir) / "params.json", "r") as f:
        params = json.loads(f.read())

    model_args: ModelArgs = ModelArgs(
        max_seq_len=max_seq_len, max_batch_size=max_batch_size, **params)
    tokenizer = Tokenizer(model_path=tokenizer_path)

    model_args.vocab_size = tokenizer.n_words
    torch.set_default_tensor_type(torch.cuda.HalfTensor)

    model = Transformer(model_args)
    torch.set_default_tensor_type(torch.FloatTensor)

    model.load_state_dict(checkpoint, strict=False)
    generator = LLaMA(model, tokenizer)
    return generator


def process(prompt: str):
    print("Received:\n", prompt)
    prompts = [prompt]
    results = generator.generate(
        prompts, max_gen_len=256, temperature=temperature, top_p=top_p
    )
    print("Generated:\n", results[0])
    return str(results[0])


def get_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt_dir", type=str,
                        default="/llama_data/7B")
    parser.add_argument("--tokenizer_path", type=str,
                        default="/llama_data/tokenizer.model")
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()

    ckpt_dir = args.ckpt_dir
    tokenizer_path = args.tokenizer_path
    temperature = 0.8
    top_p = 0.95
    max_seq_len = 512
    max_batch_size = 1

    local_rank, world_size = 0, 1
    generator = load(ckpt_dir, tokenizer_path, local_rank, world_size,
                     max_seq_len, max_batch_size)

    title = '🎉LLaMA Demo 7B🎉'
    examples = [['I believe the meaning of life is'],
                ['Simply put, the theory of relativity states that '],
                ['I am a']]
    description = '🎟Model from: [llama](https://github.com/facebookresearch/llama)\n🀄Code from：[pyllama](https://github.com/juncongmoo/pyllama)\n📌FAQ：[FAQ](https://github.com/facebookresearch/llama/blob/main/FAQ.md#2)'
    css = ".output_image, .input_image {height: 40rem !important; width: 100% !important;}"
    demo = gr.Interface(
        fn=process,
        inputs=gr.Textbox(lines=10, placeholder="Your prompt here..."),
        outputs="text",
        title=title,
        description=description,
        examples=examples,
        css=css,
        allow_flagging='never',
    )

    demo.launch(share=True, server_port=7860, enable_queue=True)
