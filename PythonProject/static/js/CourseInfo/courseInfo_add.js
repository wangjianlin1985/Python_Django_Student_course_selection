$(function () {
	$("#courseInfo_courseNumber").validatebox({
		required : true, 
		missingMessage : '请输入课程编号',
	});

	$("#courseInfo_courseName").validatebox({
		required : true, 
		missingMessage : '请输入课程名称',
	});

	$("#courseInfo_courseScore").validatebox({
		required : true,
		validType : "number",
		missingMessage : '请输入课程学分',
		invalidMessage : '课程学分输入不对',
	});

	//单击添加按钮
	$("#courseInfoAddButton").click(function () {
		//验证表单 
		if(!$("#courseInfoAddForm").form("validate")) {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		} else {
			$("#courseInfoAddForm").form({
			    url:"/CourseInfo/add",
				queryParams: {
			    	"csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val()
				},
			    onSubmit: function(){
					if($("#courseInfoAddForm").form("validate"))  { 
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
                        $("#courseInfoAddForm").form("clear");
                    }else{
                        $.messager.alert("消息",obj.message);
                        $(".messager-window").css("z-index",10000);
                    }
			    }
			});
			//提交表单
			$("#courseInfoAddForm").submit();
		}
	});

	//单击清空按钮
	$("#courseInfoClearButton").click(function () { 
		//$("#courseInfoAddForm").form("clear"); 
		location.reload()
	});
});
