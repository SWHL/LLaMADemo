#### LLaMA Demo of 7B
- πModel from: [llama](https://github.com/facebookresearch/llama)
- πCode fromοΌ[pyllama](https://github.com/juncongmoo/pyllama)
- πFAQοΌ[FAQ](https://github.com/facebookresearch/llama/blob/main/FAQ.md#2)


#### Run environ
- single GPU: 16GB


#### Use
1. Download the pretrained_model.
    - BitTorrent link: `magnet:?xt=urn:btih:ZXXDAUWYLRUXXBHUYEMS6Q5CE5WA3LVA&dn=LLaMA`
    - The final directory:
        ```text
        .
        βββ inference.py
        βββ llama
        β   βββ generation.py
        β   βββ __init__.py
        β   βββ model_parallel.py
        β   βββ model_single.py
        β   βββ tokenizer.py
        βββ LLaMA
        β   βββ 7B
        β   β   βββ checklist.chk
        β   β   βββ consolidated.00.pth
        β   β   βββ params.json
        β   βββ tokenizer_checklist.chk
        β   βββ tokenizer.model
        βββ requirements.txt
        βββ webapp_single.py
        ```
2. Install the related packages.
    ```shell
    pip install -r requirements.txt
    ```
3. Run
    - Inference by scripts
        ```shell
        python inference.py
        ```
    - Run by Gradio UI
        ```shell
        python webapp_single.py --ckpt_dir LLaMA/7B \
                                --tokenizer_path LLaMA/tokenizer.model \
                                --server_name 127.0.0.1 \
                                --server_port 7806
        ```

4. Gradio Result
   - Open `http://127.0.0.1:7860` to enjoy it.
    <div align="center">
        <img src="./assets/GradioUI.png" width="100%" height="100%">
    </div>
