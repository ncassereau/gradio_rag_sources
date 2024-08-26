from dataclasses import dataclass
from typing import List

from gradio.components.base import Component
from gradio.data_classes import GradioRootModel


@dataclass
class _RagSource:
    url: str
    retrievalScore: float
    rerankScore: float


class RAGSourcesList(GradioRootModel):
    root: List[_RagSource]


class RagSourcesTable(Component):
    data_model = RAGSourcesList

    def preprocess(self, payload: RAGSourcesList):
        """
        This docstring is used to generate the docs for this custom component.
        Parameters:
            payload: the data to be preprocessed, sent from the frontend
        Returns:
            the data after preprocessing, sent to the user's function in the backend
        """
        return payload

    def postprocess(self, value) -> RAGSourcesList:
        """
        This docstring is used to generate the docs for this custom component.
        Parameters:
            payload: the data to be postprocessed, sent from the user's function in the backend
        Returns:
            the data after postprocessing, sent to the frontend
        """
        return value

    def example_payload(self):
        return {"foo": "bar"}

    def example_value(self):
        return {"foo": "bar"}
