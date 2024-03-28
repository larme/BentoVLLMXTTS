from __future__ import annotations

import os
import pathlib

import bentoml

from utils import text2path

TTS_MODEL_ID = "tts_models/multilingual/multi-dataset/xtts_v2"

@bentoml.service(
    resources={
        "gpu": 1,
    },
    traffic={"timeout": 300},
)
class XTTS:
    def __init__(self) -> None:
        import torch
        from TTS.api import TTS

        # set GPU id here
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

        self.tts = TTS(TTS_MODEL_ID, gpu=torch.cuda.is_available())
    
    @bentoml.api
    def synthesize(
            self,
            text: str,
            lang: str,
    ) -> str:
        sample_path = "./female.wav"
        output_path = text2path(text)
        output_dir = os.path.dirname(output_path)
        pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
        if not pathlib.Path(output_path).is_file():
            self.tts.tts_to_file(
                text,
                file_path=output_path,
                speaker_wav=sample_path,
                language=lang,
                split_sentences=True,
            )
        return output_path
