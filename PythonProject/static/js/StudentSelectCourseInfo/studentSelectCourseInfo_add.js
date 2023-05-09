$(function () {
	$("#studentSelectCourseInfo_selectTime").datetimebox({
	    required : true, 
	    showSeconds: true,
	    editable: false
	});

	//单击添加按钮
	$("#studentSelectCourseInfoAddButton").click(function () {
		//验证表单 
		if(!$("#studentSelectCourseInfoAddForm").form("validate")) {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		} else {
			$("#studentSelectCourseInfoAddForm").form({
			    url:"/StudentSelectCourseInfo/add",
				queryParams: {
			    	"csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val()
				},
			    onSubmit: function(){
					if($("#studentSelectCourseInfoAddForm").form("validate"))  { 
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
                        $("#studentSelectCourseInfoAddForm").form("clear");
                    }else{
                        $.messager.alert("消息",obj.message);
                        $(".messager-window").css("z-index",10000);
                    }
			    }
			});
			//提交表单
			$("#studentSelectCourseInfoAddForm").submit();
		}
	});

	//单击清空按钮
	$("#studentSelectCourseInfoClearButton").click(function () { 
		//$("#studentSelectCourseInfoAddForm").form("clear"); 
		location.reload()
	});
});
