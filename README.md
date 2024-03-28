to start:

edit `xtts.py` and `service.py`, change lines contain `os.environ["CUDA_VISIBLE_DEVICES"] = "-1"` to proper GPU index (or keep it as "-1" to disable GPU utilization).

then:

`python3 -m venv venv && . venv/bin/activate && pip install -r requirements`

then:

`bentoml serve . -p 8000`

Request to http://0.0.0.0:8000/generate will return text and text audio url
