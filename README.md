# 심리상담 챗봇

기존 KoELECTRA 기반의 심리상담 챗봇 오픈소스를 활용하여 학습한 결과, 분류 정확도가 Test_set(전체 데이터의 10%)기준 정확도가 50%도 안나오는 현상이 발견되었습니다.
그래서 QA Pair 방식의 정확도가 높은 KcELECTRA를 이용해 학습했으나, 이 역시도 분류 정확도가 낮은 것을 확인할 수 있었습니다.

따라서, 한국어에 맞게 max_seq_length를 조정하고, 그에 맞춰 input 데이터를 전처리하는 과정을 거쳤습니다.

이후 Wandb Sweep을 활용해 Finetuning에서의 하이퍼파라미터 최적화의 목표를 두었습니다.

Pretrain 하이퍼파라미터는 따로 조정하지않았습니다. (서버 임대 기간이 20일 밖에없어 시간적 제약이 있었습니다.)
즉, 하이퍼파라미터는 KcELECTRA의 config파일을 그대로 사용했고, Batch_size = 256, Learning_rate = 2e-4로 학습을 진행했습니다.

## Pretraining - KcELECTRA (max_seq_length = 128)

해당 문서에서는 Pretraining 부분에 대해서는 다루지 않을 예정입니다. 추후 6월 이후에 코드를 정리해서 업로드 예정에있습니다.

Train 코드는 기존 [KcBERT-Finetune](https://github.com/Beomi/KcBERT-finetune)과 거의 똑같으며, Input 데이터의 Preprocessing 방법에 차이가 조금 있습니다.
따라서, 추후 업로드시에 이 부분을 중점적으로 다룰 예정이며, 코드에 대해서는 따로 블로그에 공부한 내용을 추후에 포스팅 하겠습니다.

## Data

KcELECTRA의 데이터셋이 공개되어있지않아, 네이버 뉴스의 댓글과 대댓글을 수집해 진행했습니다.

## Finetuning - KcELECTRA (max_seq_length = 128) Performance with Wellness

### Preprocessing

- Wellness_category_data : 데이터셋에서 카테고리를 분류하고 숫자로 카테고리 설정
- wellness_question_preprocess : 데이터셋에서 카테고리와, 질문(User input)만을 저장
- wellness_answer_preprocess : 데이터셋에서 답변만을 저장
- wellness_text_classification_preprocess : 카테고리 데이터와 질문(User input)데이터를 이용해 모든 질문에 숫자로 된 카테고리 할당
- seperate_Wellness_data : 전체 데이터를 train_set과 test_set 분리(test_set은 전체 데이터의 10%)

### Performance with Batch_size = [16, 32, 64, 128, 256] and Learning_rate = [1e-4, 3e-4, 1e-5, 3e-5, 1e-6, 5e-6]

- [Wandb sweep](https://wandb.ai/tkwk6428/sweep)

### Performance with Batch_size = * and Leraning_rate = CosineAnnealingWarmRestarts

- CosineAnnealingWarmUpRestarts의 변수 값을 위의 Wandb sweep이 완료된 이후 최적화할 예정입니다.

## Acknowledgement

- 서버 임대 비용은 [동국대학교 Linc+ 사업단](https://lincplus.dongguk.edu/)의 금액적인 지원을 받았습니다.

- KcELECTRA Model (max_seq_length = 128) 체크포인트를 Early stopping을 patient = 10k, delta = 0.0001을 train loss 기준으로 설정했습니다.

### KcELECTRA Model (max_seq_length = 128)을 학습하는 GPU 환경

- [네피리티](https://www.nepirity.com/): Tesla V100를 임대하여 사용 (batch_size = 16, 32, 64, 128, 256)
- [colab](https://colab.research.google.com/): Tesla k80,T4 (batch_size = 32)
- Local 3060ti (batch_size = 16)

## Requirements

- `pytorch`
- `transformers`
- `openpyxl`
- `wandb`
- `numpy`

## 한계점

- 사람의 심리상태는 359가지의 카테고리로 분류될 수 없기때문에 추가적인 심리상담 데이터 및 카테고리의 확보가 필요하다.
- sweep 결과로 보았을 때, KcELECTRA (max_seq_length = 128)만의 하이퍼파라미터가 필요한 것으로 보인다.

## Reference 

### Github Repos
- [KcELECTRA by Beomi](https://github.com/Beomi/KcELECTRA)
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
