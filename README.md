# VETTY Flask Test
[![Linkedin Badge](https://img.shields.io/badge/-shubhamsangle-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://in.linkedin.com/in/shubham-sangle)](https://in.linkedin.com/in/shubham-sangle) [![Gmail Badge](https://img.shields.io/badge/-sangleshubham9@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:sangleshubham9@gmail.com)](mailto:sangleshubham9@gmail.com)

## Dependencies
- Python3 
- Flask
- werkzeug

## Installing and Running
```
git clone https://github.com/sangleshubham/Vetty-Flask-Test.git
cd "Vetty Flask Test"
pip3 install -r requirements.txt
python3 app.py
```
## Requesting to API
- Parameters
```
/file1  -- filename 
start   -- Start Index
end     -- End Index
```
- File name supported 
```
file1
file1.txt
```
- If you know file name
```
http://127.0.0.1:5000/file1

OUT :
0: Merry is boiling matrass while Dog is meowing for coffee.

1: Jeniffer is kissing tea while Dog is meowing for kettle.

2: Frodo is barking at feather while Sam is petting feather.
truncated
149: Spotty is chewing at mug while Bill is boiling pillowcase.
```
- From-to line no
```
http://127.0.0.1:5000/file1.txt?end=10&start=0

OUT :
0: Merry is boiling matrass while Dog is meowing for coffee.
truncated
9: Tom is kissing fish while Sam is petting fish.
```

## Get what you want
All the parameter to API are optional. If dont know file name default file used for output is file1.txt

## Custom Error Handling
![image](https://user-images.githubusercontent.com/37057102/125107167-185d1300-e0fe-11eb-8d34-3cbd9140e08e.png)

