import argparse
import os
import LexerWithSingleQuoteString as LWSQS

def main():
    CodeDict = {
        "classes":[],
        "functions":[],
        "variables":[]
    }


    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="这是 systems OS app code的解释器")
    parser.add_argument("-f","--FilePath")
    args=parser.parse_args()

    file_path=args.FilePath
    file_name = os.path.basename(file_path)

    # 分离文件名和扩展名
    _ , extension = os.path.splitext(file_name)

    if not extension == ".syfee":
        return f"无法运行{file_path}，文件扩展名应为“.syfee” "
    try:
        with open(args.FilePath,"r",encoding="utf-8") as file:
            code=file.read()
    except Exception:
        with open(args.FilePath,"r",encoding="gbk") as file:
            code=file.read()

    errormeg=""
    code1=LWSQS.lexer_with_single_quote_string(code=code)
    pos=0
    while len(code1):
        type,word=code1[pos]
        if type == "ID":
            if word == "class":
                pos+=1
                t,w=code1[pos]
                if t == "ID":
                    CodeDict["classes"].append(w)
                pos+=1
                t1,w1=code1[pos]
                if not (t1=="LBRACE" and w1=="{"):
                    errormeg = """
                    File \"{path}\"  :
                        token : {pos},
                        code  : {w},
                        type  : {t}
                    
                    ErrorType: SyntaxError "class 的正确用法是：
                    class  testclass {
                        类代码
                    }
                    """.format(path=args.FilePath,pos=pos,t=t,w=w)
                    break






    if not errormeg is None:
        print(errormeg)
    

    return "exit 0"

if __name__ == "__main__":
    meg=main()
    if meg != "exit 0":
        print(meg)