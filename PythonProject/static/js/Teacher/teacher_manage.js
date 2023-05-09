var teacher_manage_tool = null; 
$(function () { 
	initTeacherManageTool(); //建立Teacher管理对象
	teacher_manage_tool.init(); //如果需要通过下拉框查询，首先初始化下拉框的值
	$("#teacher_manage").datagrid({
		url : '/Teacher/list',
		queryParams: {
			"csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val()
		},
		fit : true,
		fitColumns : true,
		striped : true,
		rownumbers : true,
		border : false,
		pagination : true,
		pageSize : 5,
		pageList : [5, 10, 15, 20, 25],
		pageNumber : 1,
		sortName : "teacherNumber",
		sortOrder : "desc",
		toolbar : "#teacher_manage_tool",
		columns : [[
			{
				field : "teacherNumber",
				title : "教师编号",
				width : 140,
			},
			{
				field : "teacherName",
				title : "教师姓名",
				width : 140,
			},
			{
				field : "teacherSex",
				title : "性别",
				width : 140,
			},
			{
				field : "teacherBirthday",
				title : "出生日期",
				width : 140,
			},
			{
				field : "teacherArriveDate",
				title : "入职日期",
				width : 140,
			},
			{
				field : "teacherPhone",
				title : "联系电话",
				width : 140,
			},
			{
				field : "teacherPhoto",
				title : "教师照片",
				width : "70px",
				height: "65px",
				formatter: function(val,row) {
					return "<img src='" + val + "' width='65px' height='55px' />";
				}
 			},
		]],
	});

	$("#teacherEditDiv").dialog({
		title : "修改管理",
		top: "50px",
		width : 700,
		height : 515,
		modal : true,
		closed : true,
		iconCls : "icon-edit-new",
		buttons : [{
			text : "提交",
			iconCls : "icon-edit-new",
			handler : function () {
				if ($("#teacherEditForm").form("validate")) {
					//验证表单 
					if(!$("#teacherEditForm").form("validate")) {
						$.messager.alert("错误提示","你输入的信息还有错误！","warning");
					} else {
						$("#teacherEditForm").form({
						    url:"/Teacher/update/" + $("#teacher_teacherNumber_edit").val(),
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
						    	console.log(data);
			                	var obj = jQuery.parseJSON(data);
			                    if(obj.success){
			                        $.messager.alert("消息","信息修改成功！");
			                        $("#teacherEditDiv").dialog("close");
			                        teacher_manage_tool.reload();
			                    }else{
			                        $.messager.alert("消息",obj.message);
			                    } 
						    }
						});
						//提交表单
						$("#teacherEditForm").submit();
					}
				}
			},
		},{
			text : "取消",
			iconCls : "icon-redo",
			handler : function () {
				$("#teacherEditDiv").dialog("close");
				$("#teacherEditForm").form("reset"); 
			},
		}],
	});
});

function initTeacherManageTool() {
	teacher_manage_tool = {
		init: function() {
		},
		reload : function () {
			$("#teacher_manage").datagrid("reload");
		},
		redo : function () {
			$("#teacher_manage").datagrid("unselectAll");
		},
		search: function() {
			var queryParams = $("#teacher_manage").datagrid("options").queryParams;
			queryParams["teacherNumber"] = $("#teacherNumber").val();
			queryParams["teacherName"] = $("#teacherName").val();
			queryParams["teacherBirthday"] = $("#teacherBirthday").datebox("getValue"); 
			queryParams["teacherArriveDate"] = $("#teacherArriveDate").datebox("getValue"); 
			queryParams["csrfmiddlewaretoken"] = $('input[name="csrfmiddlewaretoken"]').val();
			$("#teacher_manage").datagrid("options").queryParams=queryParams; 
			$("#teacher_manage").datagrid("load");
		},
		exportExcel: function() {
			$("#teacherQueryForm").form({
			    url:"/Teacher/OutToExcel?csrfmiddlewaretoken" + $('input[name="csrfmiddlewaretoken"]').val(),
			});
			//提交表单
			$("#teacherQueryForm").submit();
		},
		remove : function () {
			var rows = $("#teacher_manage").datagrid("getSelections");
			if (rows.length > 0) {
				$.messager.confirm("确定操作", "您正在要删除所选的记录吗？", function (flag) {
					if (flag) {
						var teacherNumbers = [];
						for (var i = 0; i < rows.length; i ++) {
							teacherNumbers.push(rows[i].teacherNumber);
						}
						$.ajax({
							type : "POST",
							url : "/Teacher/deletes",
							data : {
								teacherNumbers : teacherNumbers.join(","),
								"csrfmiddlewaretoken": $('input[name="csrfmiddlewaretoken"]').val()
							},
							beforeSend : function () {
								$("#teacher_manage").datagrid("loading");
							},
							success : function (data) {
								if (data.success) {
									$("#teacher_manage").datagrid("loaded");
									$("#teacher_manage").datagrid("load");
									$("#teacher_manage").datagrid("unselectAll");
									$.messager.show({
										title : "提示",
										msg : data.message
									});
								} else {
									$("#teacher_manage").datagrid("loaded");
									$("#teacher_manage").datagrid("load");
									$("#teacher_manage").datagrid("unselectAll");
									$.messager.alert("消息",data.message);
								}
							},
						});
					}
				});
			} else {
				$.messager.alert("提示", "请选择要删除的记录！", "info");
			}
		},
		edit : function () {
			var rows = $("#teacher_manage").datagrid("getSelections");
			if (rows.length > 1) {
				$.messager.alert("警告操作！", "编辑记录只能选定一条数据！", "warning");
			} else if (rows.length == 1) {
				$.ajax({
					url : "/Teacher/update/" + rows[0].teacherNumber,
					type : "get",
					data : {
						//teacherNumber : rows[0].teacherNumber,
					},
					beforeSend : function () {
						$.messager.progress({
							text : "正在获取中...",
						});
					},
					success : function (teacher, response, status) {
						$.messager.progress("close");
						if (teacher) { 
							$("#teacherEditDiv").dialog("open");
							$("#teacher_teacherNumber_edit").val(teacher.teacherNumber);
							$("#teacher_teacherNumber_edit").validatebox({
								required : true,
								missingMessage : "请输入教师编号",
								editable: false
							});
							$("#teacher_teacherName_edit").val(teacher.teacherName);
							$("#teacher_teacherName_edit").validatebox({
								required : true,
								missingMessage : "请输入教师姓名",
							});
							$("#teacher_teacherSex_edit").val(teacher.teacherSex);
							$("#teacher_teacherSex_edit").validatebox({
								required : true,
								missingMessage : "请输入性别",
							});
							$("#teacher_teacherBirthday_edit").datebox({
								value: teacher.teacherBirthday,
							    required: true,
							    showSeconds: true,
							});
							$("#teacher_teacherArriveDate_edit").datebox({
								value: teacher.teacherArriveDate,
							    required: true,
							    showSeconds: true,
							});
							$("#teacher_teacherCardNumber_edit").val(teacher.teacherCardNumber);
							$("#teacher_teacherPhone_edit").val(teacher.teacherPhone);
							$("#teacher_teacherPhotoImg").attr("src", teacher.teacherPhoto);
							$("#teacher_teacherAddress_edit").val(teacher.teacherAddress);
							$("#teacher_teacherMemo_edit").val(teacher.teacherMemo);
						} else {
							$.messager.alert("获取失败！", "未知错误导致失败，请重试！", "warning");
						}
					}
				});
			} else if (rows.length == 0) {
				$.messager.alert("警告操作！", "编辑记录至少选定一条数据！", "warning");
			}
		},
	};
}
