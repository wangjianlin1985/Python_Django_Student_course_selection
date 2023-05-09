$(function () {
    setTimeout(ajaxModifyQuery,"100");
  function ajaxModifyQuery() {	
	$.ajax({
		url : "/SpecialFieldInfo/update/" + $("#specialFieldInfo_specialFieldNumber_modify").val(),
		type : "get",
		data : {
			//specialFieldNumber : $("#specialFieldInfo_specialFieldNumber_modify").val(),
		},
		beforeSend : function () {
			$.messager.progress({
				text : "正在获取中...",
			});
		},
		success : function (specialFieldInfo, response, status) {
			$.messager.progress("close");
			if (specialFieldInfo) { 
				$("#specialFieldInfo_specialFieldNumber_modify").val(specialFieldInfo.specialFieldNumber);
				$("#specialFieldInfo_specialFieldNumber_modify").validatebox({
					required : true,
					missingMessage : "请输入专业编号",
					editable: false
				});
				$("#specialFieldInfo_specialFieldName_modify").val(specialFieldInfo.specialFieldName);
				$("#specialFieldInfo_specialFieldName_modify").validatebox({
					required : true,
					missingMessage : "请输入专业名称",
				});
				$("#specialFieldInfo_specialCollegeNumber_collegeNumber_modify").combobox({
					url:"/CollegeInfo/listAll?csrfmiddlewaretoken=" + $('input[name="csrfmiddlewaretoken"]').val(),
					method: "GET",
					valueField:"collegeNumber",
					textField:"collegeName",
					panelHeight: "auto",
					editable: false, //不允许手动输入 
					onLoadSuccess: function () { //数据加载完毕事件
						$("#specialFieldInfo_specialCollegeNumber_collegeNumber_modify").combobox("select", specialFieldInfo.specialCollegeNumberPri);
						//var data = $("#specialFieldInfo_specialCollegeNumber_collegeNumber_edit").combobox("getData"); 
						//if (data.length > 0) {
							//$("#specialFieldInfo_specialCollegeNumber_collegeNumber_edit").combobox("select", data[0].collegeNumber);
						//}
					}
				});
				$("#specialFieldInfo_specialBirthDate_modify").datebox({
					value: specialFieldInfo.specialBirthDate,
					required: true,
					showSeconds: true,
				});
				$("#specialFieldInfo_specialMan_modify").val(specialFieldInfo.specialMan);
				$("#specialFieldInfo_specialTelephone_modify").val(specialFieldInfo.specialTelephone);
				$("#specialFieldInfo_specialMemo_modify").val(specialFieldInfo.specialMemo);
			} else {
				$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
				$(".messager-window").css("z-index",10000);
			}
		}
	});

  }

	$("#specialFieldInfoModifyButton").click(function(){ 
		if ($("#specialFieldInfoModifyForm").form("validate")) {
			$("#specialFieldInfoModifyForm").form({
			    url:"SpecialFieldInfo/update/" + $("#specialFieldInfo_specialFieldNumber_modify").val(),
			    onSubmit: function(){
					if($("#specialFieldInfoEditForm").form("validate"))  {
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
			$("#specialFieldInfoModifyForm").submit();
		} else {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		}
	});
});
