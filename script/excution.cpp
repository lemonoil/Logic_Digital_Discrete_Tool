#include<bits/stdc++.h>
#include<windows.h>
using namespace std;
void read(char *res){
	static char ch;
	int len=0;
	while((ch=getchar())<'0'||ch>'9')if(ch=='m')break;
	while((ch=getchar())==' '); 
	while(ch!='M'&&ch!='\n'){
		/*if(ch>='0'&&ch<='9'){
			len++;
			res[len]=ch;
			while((ch=getchar())>='0'&&ch<='9')res[len]=ch-'0'+res[len]*10;
			if(ch=='M')break;
		}*/
		res[len++]=ch;
		ch=getchar();
	} 
	for(int i=0;i<=len;++i)cout<<res[i];cout<<endl;
} 
char command[]="python script/pyd.py ";
char LSSZ[1000];
char ss[1000];	
int main(){
	memset(LSSZ,0,sizeof(LSSZ));
	system("python script/pye.py");
	Sleep(100);
	freopen("script/tmpans.txt","r",stdin);
	read(LSSZ);
	freopen("script/another.txt","w",stdout);
	cout<<LSSZ;
	int k = strlen(command);
	for(int i=0;i<strlen(LSSZ);++i){
		command[i+k]=LSSZ[i];
		if(command[i+k]==' ')command[i+k]=',';
	}
	gets(ss);
	cin.getline(ss,80);
	ss[strlen(ss)-1]=' ';
	//cout<<ss<<endl;
	k=strlen(command);
	int op=strlen(command);
	for(int i=0;i<strlen(command);++i){
		if(command[i]==','&&(command[i+1]<'0'||command[i+1]>'9'))command[i]=' ',command[i+1]='\0',op=i;
	}
	//cout<<command<<endl; 
	for(int i=0;i<strlen(ss);++i){
		command[i+op+1]=ss[i];
	}
	command[strlen(ss)+op+1]='\00';
	system(command);
//	cout<<command<<endl;
	return 0;
}
