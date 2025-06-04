from openai import OpenAI
from openaikey import OPENAI_KEY

client = OpenAI(api_key=OPENAI_KEY)


def get_prompt(prompt,system_prompt='',messages = []):

    if system_prompt != '' and messages == []: 
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    try :
        response = client.responses.create(
        model="gpt-4.1",
        input=messages)
        text =response.output_text
        messages.append({"role": "user", "content": text})
        return text
    except Exception as e:
        print('OpenAI exception' + str(e))
        return e
    return None


if __name__ == '__main__':
    print(get_prompt('parlez moi de Thales et de son histoire'))
