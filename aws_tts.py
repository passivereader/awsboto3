# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly/client/synthesize_speech.html
# FreeBSD: consider pkg install py39-awscli
# https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html
# https://docs.aws.amazon.com/polly/latest/dg/SynthesizeSpeechSamplePython.html
# pip install boto3
# IAM: create a user, there is a AWS-managed permission set for Polly
# IAM: limit user within permission boundary
# ~/.aws/credentials and ~/.aws/config, see boto3 docs Quickstart section

import boto3

client = boto3.client('polly')
# describe_voices()

example_text = "Hello"

response = client.synthesize_speech(
    Engine="standard",
    LanguageCode="en-AU",
    OutputFormat="mp3",
    SampleRate="8000",
    Text=example_text,
    TextType="text",
    VoiceId="Nicole")

with open('output.mp3', 'wb') as file:
    file.write(response['AudioStream'].read())

client.close()
