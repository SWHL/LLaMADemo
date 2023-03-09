#### LLaMA Demo of 7B
- 🎟Model from: [llama](https://github.com/facebookresearch/llama)
- 🀄Code from：[pyllama](https://github.com/juncongmoo/pyllama)
- 📌FAQ：[FAQ](https://github.com/facebookresearch/llama/blob/main/FAQ.md#2)


#### Run environ
- single GPU: 16GB


#### Use
1. Download the pretrained_model.
    - BitTorrent link: `magnet:?xt=urn:btih:ZXXDAUWYLRUXXBHUYEMS6Q5CE5WA3LVA&dn=LLaMA`
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
        python webapp_single.py
        ```

4. Gradio Result
    <div align="center">
        <img src="./assets/GradioUI.png" width="100%" height="100%">
    </div>
