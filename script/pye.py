from tkinter import *
import tkinter.messagebox as messagebox

inputString = '' #输入的命题公式字符串
funcString = '' #c存放符号替换后的公式字符串
nvariable = [] #变量数量
Orstring = [] #主析取范式最小项
Andstring = [] #主合取范式最大项
former = '' #符号前面的部分
latter = '' #符号后面的部分
Orresult = ''
Andresult = ''

#提取变量，判断输入
def getVariable():
	global inputString, nvariable, charCount
	for c in inputString:
		if c >= 'A' and c <= 'Z' or c >= 'a' and c <= 'z': #提取变量
			if c not in nvariable:
				nvariable.append(c)
		elif c!='!' and c!= "'" and c != '~' and c != '&' and c != '|' and c != '>' and c != '#' and c != '@' and c != '$' and c != '*' and c != '(' and c != ')' :
			print('There is something wrong in your input string.')
	nvariable = sorted(nvariable)

#处理>,#,@,$,*
def func(c):
	global inputString, funcString, former, latter
	slen = len(funcString)
	#遍历字符串
	
	for i in range(0,slen):
		if funcString[i] is c:
			#找到former
			if funcString[i-1] is not  ')':
				if funcString[i-2] is not '~':
					former = funcString[i-1]
				else:
					former = funcString[i-2:i]
			else:
				flag = 1
				j = i-1-1
				while flag != 0 and j >= 0:
					if funcString[j] is ')':
						flag += 1
						j -= 1
					elif funcString[j] is '(':
						flag -= 1
						j -= 1
					else:
						j -= 1
				former = funcString[j+1:i]

#			print(former)

			#找到latter
			if funcString[i+1] is not  '~':
				if funcString[i+1] is not '(':
					latter = funcString[i+1]
				else:
					flag = 1
					j = i+1+1
					while flag != 0 and j < slen: 
						if funcString[j] is '(':
							flag += 1
							j += 1
						elif funcString[j] is ')':
							flag -= 1
							j += 1
						else:
							j += 1
					latter = funcString[i+1:j]
			else:
				if funcString[i+2] is not '(':
					latter = funcString[i+1:i+3]
				else:
					flag = 1
					j = i+2+1
					while flag != 0 and j < slen:
						if funcString[j] is '(':
							flag += 1
							j += 1
						elif funcString[j] is ')':
							flag -= 1
							j += 1
						else:
							j += 1
					latter = funcString[i+1:j]			#符号替换

#			print(latter)

			if c is '>':
				funcString = funcString.replace(former+'>'+latter, '('+'~'+former+'|'+latter+')')
			if c is '#':
				funcString = funcString.replace(former+'#'+latter, '(('+former+'&'+latter+')|('+'~'+former+'&'+'~'+latter+'))')
			if c is '@':
				funcString = funcString.replace(former+'@'+latter, '(('+former+'&'+'~'+latter+')|('+'~'+former+'&'+latter+'))')
			if c is '$':
				funcString = funcString.replace(former+'$'+latter, '~'+'('+former+'&'+latter+')')
			if c is '*':
				funcString = funcString.replace(former+'*'+latter, '~'+'('+former+'|'+latter+')')
			func(c)

#		print(i, slen)
#统一标准
def singleStander():
	global inputString
	slen = len(inputString)
	#遍历字符串
	reString = ""
	leftBracket = {'in':'SEU'}
	rightBracket = {'name':'lemonoil'}
	leftCnt = 0
	rightCnt = 0
	for i in range(0,slen):
		if inputString[i] is '!':
			reString+='~'
		else:
			reString+=inputString[i]
	inputString=reString+'`'
	#print(inputString)
	reString=''
	for i in range(0,slen):
		if inputString[i] is '(': 
			leftCnt+=1
			leftBracket[i] = leftCnt
		if inputString[i] is ')':
			rightCnt+=1
			rightBracket[rightCnt] = i
	for i in range(0,slen):
		if inputString[i] is "'":
		#无事发生
			Franch=0
			#print("Franch")
		elif inputString[i] is not '(' and inputString[i] is not ')':
			if inputString[i+1] is not '\'':
				reString+=inputString[i]
			else :
				reString+='~'+inputString[i]
				i+=1
		else :
			if inputString[i] is '(' and inputString[rightBracket[leftBracket[i]]+1] is "'" :
				reString+='~'+inputString[i]
			else :
				reString +=inputString[i]

	#print(reString)
	#print(inputString)
	inputString = reString
#符号替换
def input2func():
	global inputString, funcString
	funcString = inputString
	func('>') #蕴涵
	func('#') #等价
	func('@') #异或
	func('$') #与非
	func('*') #或非

#利用真值表法计算主析取范式和主合取范式
def binaryCal():
	global inputString, funcString, nvariable, Orstring, Andstring
	nlen = len(nvariable) #变量个数
	n = 2 ** nlen #所有情况的个数
	#获取真值表。赋值计算
	for i in range(0,n):
		value = [] #赋值
		nowline = i #当前行数
		for j in range(0,nlen):
			value.append(0) #占位
			value[j] = nowline%2
			nowline = nowline//2
		value.reverse()
		value = list(map(str, value))
		strv = funcString
		for k in range(0,nlen):
			strv = strv.replace(nvariable[k], value[k])
		result = eval(strv)&1
		#判断是最大项还是最小项
		if result == 1:
			Orstring.append(i) #最小项
		else:
			Andstring.append(i) #最大项

#输出主析取范式和主合取范式
def myoutput():
	global Orstring, Andstring, Orresult, Andresult
	AndOrchar='m '
	#print('主析取范式：')
	for i in range(0,len(Orstring)):
		AndOrchar += str(Orstring[i])+' '
		Orresult += ('m' + str(Orstring[i]) +' ')
	f=open("script/tmpans.txt","w",encoding='utf-8')
	#f.write(Orchar)
	AndOrchar+='\nM '
	#print('主合取范式：')
	for i in range(len(Andstring)):
		#print('M'+str(Andstring[i]),sep='')
		AndOrchar += str(Andstring[i]) + ' '
		Andresult += ('M' + str(Andstring[i]) +' ')
	AndOrchar+='\n'
	f.write(AndOrchar)
	nvariablePrint = '-v ' 
	for c in nvariable:
		nvariablePrint += c+','
	f.write(nvariablePrint)
	f.close()

#主函数
def main():
	global Orresult, Andresult
	#myinput()
	getVariable()
	input2func()
	#如果输入错误，则在赋值函数中会出错，抛出错误，显示"wrong"
	try:
		binaryCal()
	except Exception as e:
		print('Error:', e)
		Orresult = 'input wrong!'
		Andresult = '-_-'
	else:
		myoutput()
	finally:
		show()


#显示
def show():
	global Orresult, Andresult, inputString, nvariable, funcString, Orstring, Andstring, former, latter
#	StringO1.config(text=Orresult)
#	StringO2.config(text=Andresult)
	#清空储存数据，为下一次做准备
	inputString = ''
	funcString = ''
	nvariable = []
	Orstring = []
	Andstring = []
	Orresult = ''
	Andresult = ''
	former = ''
	latter = ''

def init():
	global inputString,StringIn, StringO1, StringO2
	f=open("script/quespy.txt","r")
	inputString=f.read()
	#inputString='a&b|a&c'
	#print(inputString)
	f.close()
	singleStander()
	#print(inputString)

if __name__ == '__main__':
	init()
	main()
	
