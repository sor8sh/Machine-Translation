Machine-Translation

1. ``git clone https://github.com/OpenNMT/OpenNMT-py``

2. ``cd OpenNMT-py``

3. ``pip3 install -r requirements.txt``

4. Preprocess the data: 

    ``python3 preprocess.py -train_src data/src-train.txt -train_tgt data/tgt-train.txt -valid_src data/src-val.txt -valid_tgt data/tgt-val.txt -save_data data/demo``

5. Train the model: 
    
    ``python3 train.py -data data/demo -save_model demo-model``

6. Translate: 

    ``python3 translate.py -model demo-model_XYZ.pt -src data/src-test.txt -output pred.txt -replace_unk -verbose``