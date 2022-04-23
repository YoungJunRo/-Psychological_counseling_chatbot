import torch
import random

from transformers import  AutoConfig, AutoTokenizer
from electra_model import ElectraForSequenceClassification,electra_input

def load_data():
  category_path = f"./data/wellness_category.txt"
  answer_path = f"./data/wellness_ans.txt"

  c_f, a_f = open(category_path,'r'), open(answer_path,'r')

  category_lines, answer_lines = c_f.readlines(), a_f.readlines()

  category, answer = {}, {}
  for line_num, line_data in enumerate(category_lines):
    data = line_data.split('    ')
    category[data[1][:-1]]=data[0]

  for line_num, line_data in enumerate(answer_lines):
    data = line_data.split('    ')
    keys = answer.keys()
    if(data[0] in keys):
      answer[data[0]] += [data[1][:-1]]
    else:
      answer[data[0]] =[data[1][:-1]]

  return category, answer

if __name__ == "__main__":
    data = f"./data/wellness_text_classification.txt"
    finetuned_model = f"./finetuned_model/psychological_counseling_model.pth"
    pretrained_model = "./pretrained_model"
    category, answer = load_data()

    ctx = "cuda"
    device = torch.device(ctx)
    checkpoint = torch.load(finetuned_model, map_location=device)
    tokenizer = AutoTokenizer.from_pretrained(pretrained_model)
    electra_config = AutoConfig.from_pretrained(pretrained_model)

    model = ElectraForSequenceClassification.from_pretrained(pretrained_model_name_or_path=pretrained_model,
                                                                config=electra_config,
                                                                num_labels=359)
    model.load_state_dict(checkpoint['model_state_dict'])
    model.to(device)
    model.eval()


    while True:
        userinput = input('user: ')
        if '종료' == userinput:
          break
        else:
          data = electra_input(tokenizer, userinput, device, 128)

          output = model(**data)

          logit = output[0]
          softmax_logit = torch.softmax(logit, dim=-1)
          softmax_logit = softmax_logit.squeeze()

          max_index = torch.argmax(softmax_logit).item()
          max_index_value = softmax_logit[torch.argmax(softmax_logit)].item()

          answer_list = answer[category[str(max_index)]]
          answer_len = len(answer_list) - 1
          answer_index = random.randint(0, answer_len)
          print(f'bot: {answer_list[answer_index]}, index_value: {max_index_value}')
          print('argmin:',softmax_logit[torch.argmin(softmax_logit)])