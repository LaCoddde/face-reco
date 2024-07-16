# face-reco

face-reco/
├── README.md
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── face_ctrl.py
│   │   ├── doc_ctrl.py
│   │   ├── compare_ctrl.py
│   │   ├── obj_ctrl.py
│   │   ├── ocr_ctrl.py
│   │   ├── account_ctrl.py
│   │   └── report_ctrl.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── api_key.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── face_svc.py
│   │   ├── doc_svc.py
│   │   ├── compare_svc.py
│   │   ├── obj_svc.py
│   │   ├── ocr_svc.py
│   │   ├── account_svc.py
│   │   └── report_svc.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── face_recog.py
│   │   ├── doc_proc.py
│   │   ├── compare.py
│   │   ├── obj_detect.py
│   │   ├── ocr.py
│   │   └── security.py
│   ├── static/
│   │   └── sample_images/
│   ├── templates/
│   └── tests/
│       ├── __init__.py
│       ├── test_face.py
│       ├── test_doc.py
│       ├── test_compare.py
│       ├── test_obj.py
│       ├── test_ocr.py
│       ├── test_account.py
│       └── test_report.py
└── docs/
    ├── api_doc.md
    └── dev_guide.md
