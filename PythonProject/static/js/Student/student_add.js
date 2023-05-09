$(function () {
	$("#student_studentNumber").validatebox({
		required : true, 
		missingMessage : '请输入学号',
	});

	$("#student_studentName").validatebox({
		required : true, 
		missingMessage : '请输入姓名',
	});

	$("#student_studentPassword").validatebox({
		required : true, 
		missingMessage : '请输入登录密码',
	});

	$("#student_studentSex").validatebox({
		required : true, 
		missingMessage : '请输入性别',
	});

	$("#student_studentBirthday").datebox({
	    required : true, 
	    showSeconds: true,
	    editable: false
	});

	//单击添加按钮
	$("#studentAddButton").click(function () {
		//验证表单 
		if(!$("#studentAddForm").form("validate")) {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		} else {
			$("#studentAddForm").form({
			    url:"/Student/add",
				queryParams: {
			    	"csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val()
				},
			    onSubmit: function(){
					if($("#studentAddForm").form("validate"))  { 
	                	$.messager.progress({
							text : "正在提交数据中...",
						}); 
	                	return true;
	                } else {
	                    return false;
	                }
			    },
			    success:function(data){
			    	$.messager.progress("close");
                    //此处data={"Success":true}是字符串
                	var obj = jQuery.parseJSON(data); 
                    if(obj.success){ 
                        $.messager.alert("消息","保存成功！");
                        $(".messager-window").css("z-index",10000);
                        $("#studentAddForm").form("clear");
                    }else{
                        $.messager.alert("消息",obj.message);
                        $(".messager-window").css("z-index",10000);
                    }
			    }
			});
			//提交表单
			$("#studentAddForm").submit();
		}
	});

	//单击清空按钮
	$("#studentClearButton").click(function () { 
		//$("#studentAddForm").form("clear"); 
		location.reload()
	});
});
