$(function () {
    setTimeout(ajaxModifyQuery,"100");
  function ajaxModifyQuery() {	
	$.ajax({
		url : "/CollegeInfo/update/" + $("#collegeInfo_collegeNumber_modify").val(),
		type : "get",
		data : {
			//collegeNumber : $("#collegeInfo_collegeNumber_modify").val(),
		},
		beforeSend : function () {
			$.messager.progress({
				text : "正在获取中...",
			});
		},
		success : function (collegeInfo, response, status) {
			$.messager.progress("close");
			if (collegeInfo) { 
				$("#collegeInfo_collegeNumber_modify").val(collegeInfo.collegeNumber);
				$("#collegeInfo_collegeNumber_modify").validatebox({
					required : true,
					missingMessage : "请输入学院编号",
					editable: false
				});
				$("#collegeInfo_collegeName_modify").val(collegeInfo.collegeName);
				$("#collegeInfo_collegeName_modify").validatebox({
					required : true,
					missingMessage : "请输入学院名称",
				});
				$("#collegeInfo_collegeBirthDate_modify").datebox({
					value: collegeInfo.collegeBirthDate,
					required: true,
					showSeconds: true,
				});
				$("#collegeInfo_collegeMan_modify").val(collegeInfo.collegeMan);
				$("#collegeInfo_collegeTelephone_modify").val(collegeInfo.collegeTelephone);
				$("#collegeInfo_collegeMemo_modify").val(collegeInfo.collegeMemo);
			} else {
				$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
				$(".messager-window").css("z-index",10000);
			}
		}
	});

  }

	$("#collegeInfoModifyButton").click(function(){ 
		if ($("#collegeInfoModifyForm").form("validate")) {
			$("#collegeInfoModifyForm").form({
			    url:"CollegeInfo/update/" + $("#collegeInfo_collegeNumber_modify").val(),
			    onSubmit: function(){
					if($("#collegeInfoEditForm").form("validate"))  {
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
			$("#collegeInfoModifyForm").submit();
		} else {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		}
	});
});
