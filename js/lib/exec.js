var exec = require("child_process").exec;
function myTest() {

    return new Promise(function(resolve, reject) {
        //script\\excution.exe
        let fs=require("fs");
        var textLs = $("#varBoxA").val();
        fs.writeFile("script/quespy.txt",textLs,(err,data) => {
            if(err){
                console.log(err);
            }else{
                console.log(textLs);
            }

        });
        //sleep(1000);
        var cmd = "script\\excution.exe";
        exec(cmd,{
            maxBuffer: 1024 * 2000
        }, function(err, stdout, stderr) {
            if (err) {
                console.log(err);
                reject(err);
            } else if (stderr.lenght > 0) {
                reject(new Error(stderr.toString()));
            } else {
                console.log(stdout);
                resolve();
            }
        });
        //sleep(100);
        fs.readFile("script/anspy.txt",'utf-8',(err,data) => {
            if(err){
                console.log(err);
            }else{
                console.log(data)
                console.log("file success！！！")
                $("#varBoxB").html(data);
            }

        });
        fs.readFile("script/another.txt",'utf-8',(err,data) => {
            if(err){
                console.log(err);
            }else{
                console.log(data)
                console.log("file success！！！")
                $("#varBoxC").html(data);
            }

        });
        // fs.("script/anspy.txt",'utf-8',(err,data) => {
        //     if(err){
        //         console.log(err);
        //     }else{
        //         console.log(data)
        //         console.log("file success！！！")
        //         $("#varBoxB").html(data);
        //     }

        // });
    });
};
var fs = require("fs");
function textLoad(){
    fs.readFile("test.txt", 'utf-8', (err, data) => {
        if (err) throw err;
        console.log(data)
    });
};
function sleep(numberMillis) {
	var now = new Date();
	var exitTime = now.getTime() + numberMillis;
	while (true) {
		now = new Date();
		if (now.getTime() > exitTime)
		return;
	}
};
//module.exports = function myTest()
//const execOne = document.getElementById("pye").addEventListener("click",myTest());
