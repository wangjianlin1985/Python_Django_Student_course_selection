$(function () {
    setTimeout(ajaxModifyQuery,"100");
  function ajaxModifyQuery() {	
	$.ajax({
		url : "/Teacher/update/" + $("#teacher_teacherNumber_modify").val(),
		type : "get",
		data : {
			//teacherNumber : $("#teacher_teacherNumber_modify").val(),
		},
		beforeSend : function () {
			$.messager.progress({
				text : "正在获取中...",
			});
		},
		success : function (teacher, response, status) {
			$.messager.progress("close");
			if (teacher) { 
				$("#teacher_teacherNumber_modify").val(teacher.teacherNumber);
				$("#teacher_teacherNumber_modify").validatebox({
					required : true,
					missingMessage : "请输入教师编号",
					editable: false
				});
				$("#teacher_teacherName_modify").val(teacher.teacherName);
				$("#teacher_teacherName_modify").validatebox({
					required : true,
					missingMessage : "请输入教师姓名",
				});
				$("#teacher_teacherSex_modify").val(teacher.teacherSex);
				$("#teacher_teacherSex_modify").validatebox({
					required : true,
					missingMessage : "请输入性别",
				});
				$("#teacher_teacherBirthday_modify").datebox({
					value: teacher.teacherBirthday,
					required: true,
					showSeconds: true,
				});
				$("#teacher_teacherArriveDate_modify").datebox({
					value: teacher.teacherArriveDate,
					required: true,
					showSeconds: true,
				});
				$("#teacher_teacherCardNumber_modify").val(teacher.teacherCardNumber);
				$("#teacher_teacherPhone_modify").val(teacher.teacherPhone);
				$("#teacher_teacherPhotoImgMod").attr("src", teacher.teacherPhoto);
				$("#teacher_teacherAddress_modify").val(teacher.teacherAddress);
				$("#teacher_teacherMemo_modify").val(teacher.teacherMemo);
			} else {
				$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
				$(".messager-window").css("z-index",10000);
			}
		}
	});

  }

	$("#teacherModifyButton").click(function(){ 
		if ($("#teacherModifyForm").form("validate")) {
			$("#teacherModifyForm").form({
			    url:"Teacher/update/" + $("#teacher_teacherNumber_modify").val(),
			    onSubmit: function(){
					if($("#teacherEditForm").form("validate"))  {
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
                	var obj = jQuery.parseJSON(data);
                    if(obj.success){
                        $.messager.alert("消息","信息修改成功！");
                        $(".messager-window").css("z-index",10000);
                        //location.href="frontlist";
                    }else{
                        $.messager.alert("消息",obj.message);
                        $(".messager-window").css("z-index",10000);
                    } 
			    }
			});
			//提交表单
			$("#teacherModifyForm").submit();
		} else {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		}
	});
});
