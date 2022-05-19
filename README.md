# 심리상담 챗봇

## Pre_training - KcELECTRA (max_seq_length = 128)

### preprocessing
대부분의 한국어의 길이가 128자가 안되는점을 고려하여 128자가 넘는 문장은 말뭉치에서 제외하거나, 2문장으로 나누어 학습한다.

###

KcELECTRA 학습하는 코드와 데이터 전처리 과정은 추후 업로드 예정입니다. 
(궁금하신 분들은 기존 max_seq_length = 512인 KcELECTRA의 학습코드를 미리 보시는 것을 추천드립니다.)

### Fine_tuning - KcELECTRA (max_seq_length = 128) Performance with Wellness conversation dataset

## preprocessing

## Performance with Batch_size = [16, 32, 64, 128, 256] and Learning_rate = [1e-4, 3e-4, 1e-5, 3e-5, 1e-6, 5e-6]

[Wandb sweep]https://wandb.ai/tkwk6428/sweep

## Performance with Batch_size = * and Leraning_rate = CosineAnnealingWarmRestarts

CosineAnnealingWarmUpRestarts의 변수 값을 위의 Wandb sweep이 완료된 이후 최적화할 예정입니다.

## Acknowledgement

KcELECTRA Model (max_seq_length = 128)을 학습하는 GPU 환경은 [네피리티](https://www.nepirity.com/)의 Tesla V100를 임대하여 사용했습니다.

서버 임대 비용은 [동국대학교 Linc+ 사업단](https://lincplus.dongguk.edu/)의 금액적인 지원을 받았습니다.

KcELECTRA Model (max_seq_length = 128) 체크포인트를 Early stopping을 patient = 10k, delta = 0.001을 train loss 기준으로 설정했습니다.

KcELECTRA 학습하는 코드와 데이터 전처리 과정은 추후 업로드 예정입니다. 
(궁금하신 분들은 기존 max_seq_length = 512인 KcELECTRA의 학습코드를 미리 보시는 것을 추천드립니다.)

KcELECTRA with Wellness

## Requirements

- `pytorch`
- `transformers`
- `openpyxl`
- `wandb`
- `numpy`

## Reference 

### Github Repos
- [KcELECTRA by Beomi](https://github.com/Beomi/KcELECTRA)
- [BERT by Google](https://github.com/google-research/bert)
- [KoBERT by SKT](https://github.com/SKTBrain/KoBERT)
- [KoELECTRA by Monologg](https://github.com/monologg/KoELECTRA/)
- [Transformers by Huggingface](https://github.com/huggingface/transformers)
- [Tokenizers by Hugginface](https://github.com/huggingface/tokenizers)
- [ELECTRA train code by KLUE](https://github.com/KLUE-benchmark/KLUE-ELECTRA)
- [Korean Language Model for Wellness Conversation](https://github.com/nawnoes/WellnessConversation-LanguageModel/)
- [Wandb Example for pytorch](https://github.com/wandb/examples/tree/master/examples/pytorch)

### Blogs

- [Monologg님의 KoELECTRA 학습기](https://monologg.kr/categories/NLP/ELECTRA/)
- [김진솔님의 Pytorch Learning Rate Scheduler (러닝 레이트 스케쥴러) 정리](https://gaussian37.github.io/dl-pytorch-lr_scheduler/)

### Dataset

- [웰니스 대화 스크립트 데이터셋](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-006)
