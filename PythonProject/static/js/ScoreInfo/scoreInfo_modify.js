$(function () {
    setTimeout(ajaxModifyQuery,"100");
  function ajaxModifyQuery() {	
	$.ajax({
		url : "/ScoreInfo/update/" + $("#scoreInfo_scoreId_modify").val(),
		type : "get",
		data : {
			//scoreId : $("#scoreInfo_scoreId_modify").val(),
		},
		beforeSend : function () {
			$.messager.progress({
				text : "正在获取中...",
			});
		},
		success : function (scoreInfo, response, status) {
			$.messager.progress("close");
			if (scoreInfo) { 
				$("#scoreInfo_scoreId_modify").val(scoreInfo.scoreId);
				$("#scoreInfo_scoreId_modify").validatebox({
					required : true,
					missingMessage : "请输入记录编号",
					editable: false
				});
				$("#scoreInfo_studentNumber_studentNumber_modify").combobox({
					url:"/Student/listAll?csrfmiddlewaretoken=" + $('input[name="csrfmiddlewaretoken"]').val(),
					method: "GET",
					valueField:"studentNumber",
					textField:"studentName",
					panelHeight: "auto",
					editable: false, //不允许手动输入 
					onLoadSuccess: function () { //数据加载完毕事件
						$("#scoreInfo_studentNumber_studentNumber_modify").combobox("select", scoreInfo.studentNumberPri);
						//var data = $("#scoreInfo_studentNumber_studentNumber_edit").combobox("getData"); 
						//if (data.length > 0) {
							//$("#scoreInfo_studentNumber_studentNumber_edit").combobox("select", data[0].studentNumber);
						//}
					}
				});
				$("#scoreInfo_courseNumber_courseNumber_modify").combobox({
					url:"/CourseInfo/listAll?csrfmiddlewaretoken=" + $('input[name="csrfmiddlewaretoken"]').val(),
					method: "GET",
					valueField:"courseNumber",
					textField:"courseName",
					panelHeight: "auto",
					editable: false, //不允许手动输入 
					onLoadSuccess: function () { //数据加载完毕事件
						$("#scoreInfo_courseNumber_courseNumber_modify").combobox("select", scoreInfo.courseNumberPri);
						//var data = $("#scoreInfo_courseNumber_courseNumber_edit").combobox("getData"); 
						//if (data.length > 0) {
							//$("#scoreInfo_courseNumber_courseNumber_edit").combobox("select", data[0].courseNumber);
						//}
					}
				});
				$("#scoreInfo_scoreValue_modify").val(scoreInfo.scoreValue);
				$("#scoreInfo_scoreValue_modify").validatebox({
					required : true,
					validType : "number",
					missingMessage : "请输入成绩得分",
					invalidMessage : "成绩得分输入不对",
				});
				$("#scoreInfo_studentEvaluate_modify").val(scoreInfo.studentEvaluate);
			} else {
				$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
				$(".messager-window").css("z-index",10000);
			}
		}
	});

  }

	$("#scoreInfoModifyButton").click(function(){ 
		if ($("#scoreInfoModifyForm").form("validate")) {
			$("#scoreInfoModifyForm").form({
			    url:"ScoreInfo/update/" + $("#scoreInfo_scoreId_modify").val(),
			    onSubmit: function(){
					if($("#scoreInfoEditForm").form("validate"))  {
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
			$("#scoreInfoModifyForm").submit();
		} else {
			$.messager.alert("错误提示","你输入的信息还有错误！","warning");
			$(".messager-window").css("z-index",10000);
		}
	});
});
