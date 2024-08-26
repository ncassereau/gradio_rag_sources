import gradio as gr

from gradio_rag_sources import RagSourcesTable
from gradio_rag_sources import _RagSource as RagSource


with gr.Blocks() as demo:
    sources = [
        RagSource(
            url="https://www.idris.fr",
            retrievalScore=0.45,
            rerankScore=0.9,
        ),
        RagSource(
            url="https://www.google.fr",
            retrievalScore=0.45,
            rerankScore=0.95,
        ),
        RagSource(
            url="https://www.pytorch.org",
            retrievalScore=0.55,
            rerankScore=0.8,
        ),
    ]
    RagSourcesTable(value=sources)


if __name__ == "__main__":
    demo.launch()
