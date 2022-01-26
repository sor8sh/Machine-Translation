# Machine-Translation

> This repository is made for the NLP course project - May 2018.

* Translating Persian text to Quran-style Arabic text using [OpenNMT-py](https://github.com/OpenNMT/OpenNMT-py).

---

To run, follow these steps:

1. Clone OpenNMT-py: <br>
``git clone https://github.com/OpenNMT/OpenNMT-py``<br>
``cd OpenNMT-py``

2. Intall requirements: <br>
``pip3 install -r requirements.txt``

3. Preprocess the data: <br>
``python3 preprocess.py -train_src data/src-train.txt -train_tgt data/tgt-train.txt -valid_src data/src-val.txt -valid_tgt data/tgt-val.txt -save_data data/demo``

4. Train the model: <br>
``python3 train.py -data data/demo -save_model demo-model``

6. Translate: <br>
``python3 translate.py -model demo-model_XYZ.pt -src data/src-test.txt -output pred.txt -replace_unk -verbose``

---

Sample result:

        input: من شما را دوست دارم
        output: إِنِّي لَكُمْ أَمِينٌ 
