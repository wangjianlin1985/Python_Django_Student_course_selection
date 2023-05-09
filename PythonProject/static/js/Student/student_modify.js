$(function () {
    setTimeout(ajaxModifyQuery,"100");
  function ajaxModifyQuery() {	
	$.ajax({
		url : "/Student/update/" + $("#student_studentNumber_modify").val(),
		type : "get",
		data : {
			//studentNumber : $("#student_studentNumber_modify").val(),
		},
		beforeSend : function () {
			$.messager.progress({
				text : "正在获取中...",
			});
		},
		success : function (student, response, status) {
			$.messager.progress("close");
			if (student) { 
				$("#student_studentNumber_modify").val(student.studentNumber);
				$("#student_studentNumber_modify").validatebox({
					required : true,
					missingMessage : "请输入学号",
					editable: false
				});
				$("#student_studentName_modify").val(student.studentName);
				$("#student_studentName_modify").validatebox({
					required : true,
					missingMessage : "请输入姓名",
				});
				$("#student_studentPassword_modify").val(student.studentPassword);
				$("#student_studentPassword_modify").validatebox({
					required : true,
					missingMessage : "请输入登录密码",
				});
				$("#student_studentSex_modify").val(student.studentSex);
				$("#student_studentSex_modify").validatebox({
					required : true,
					missingMessage : "请输入性别",
				});
				$("#student_studentClassNumber_classNumber_modify").combobox({
					url:"/ClassInfo/listAll?csrfmiddlewaretoken=" + $('input[name="csrfmiddlewaretoken"]').val(),
					method: "GET",
					valueField:"classNumber",
					textField:"className",
					panelHeight: "auto",
					editable: false, //不允许手动输入 
					onLoadSuccess: function () { //数据加载完毕事件
						$("#student_studentClassNumber_classNumber_modify").combobox("select", student.studentClassNumberPri);
						//var data = $("#student_studentClassNumber_classNumber_edit").combobox("getData"); 
						//if (data.length > 0) {
							//$("#student_studentClassNumber_classNumber_edit").combobox("select", data[0].classNumber);
						//}
					}
				});
				$("#student_studentBirthday_modify").datebox({
					value: student.studentBirthday,
					required: true,
					showSeconds: true,
				});
				$("#student_studentState_modify").val(student.studentState);
				$("#student_studentPhotoImgMod").attr("src", student.studentPhoto);
				$("#student_studentTelephone_modify").val(student.studentTelephone);
				$("#student_studentEmail_modify").val(student.studentEmail);
				$("#student_studentQQ_modify").val(student.studentQQ);
				$("#student_studentAddress_modify").val(student.studentAddress);
				$("#student_studentMemo_modify").val(student.studentMemo);
			} else {
				$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
				$(".messager-window").css("z-index",10000);
			}
		}
	});

  }

	$("#studentModifyButton").click(function(){ 
		if ($("#studentModifyForm").form("validate")) {
			$("#studentModifyForm").form({
			    url:"Student/update/" + $("#student_studentNumber_modify").val(),
			    onSubmit: function(){
					if($("#studentEditForm").form("validate"))  {
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
			$("#studentModifyForm").submit();
		} else {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		}
	});
});
