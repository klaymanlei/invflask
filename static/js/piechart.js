function drawPieChart(chartname, charttitle) {
	var myChart = echarts.init(document.getElementById(chartname));
	var php_url = "php/" + chartname + ".php";
	
	function formatedDate() {
		var now = new Date();
		var dt_str = now.getFullYear();
		dt_str = dt_str + "-";
		if (now.getMonth() + 1 >= 10)
			dt_str = dt_str + (now.getMonth() + 1);
		else 
			dt_str = dt_str + "0" + (now.getMonth() + 1);
		if (now.getDate() >= 10)
			dt_str = dt_str + "-" + now.getDate();
		else 
			dt_str = dt_str + "-" + "0" + now.getDate();
		return dt_str;
	}
	var dt_str = formatedDate();

	var option = {
		animation: false,
		title: {
			textStyle: {
				fontSize: 14,
				color:'#ddd'
			},
			text: charttitle
		},
        grid:{
            x:20,
            y:40,
            x2:20,
            y2:20
        },		
		color: ['#66d', '#6d6', '#d66', '#6dd', '#d6d', '#dd6', '#d96'],
		backgroundColor: '#000',
		tooltip : {
			//formatter: "{a} <br/>{b} : {c}%"
			formatter: "{b}: {c}%"
		},
		label: {
			normal: {
				//position: 'inside',
				fontSize: 8
			}
		},
		labelLine: {
			normal: {
				//position: 'inside',
				length2: 1
			}
		},
		series: [
			{
				name: 'HDFS磁盘空间',
				type: 'pie',
				center : ['35%', '60%'],
				radius: ['0%', '70%'],
			}
//			,{
//				name: '磁盘占用增长',
//				type: 'pie',
//				center : ['65%', '60%'],
//				radius: ['40%', '70%'],
//				label: {
//					normal: {
//						show: false
//					}
//				},
//				data: [{name: 'a',value:22},{name: 'b',value:32}]
//			}
		]
	};

	myChart.setOption(option);

	$.ajax({
		type: "GET",
		async: true,
		url: php_url,
		data: {date:dt_str},
		dataType: "json",
		success: function(rs){
			option = {
				series: rs[0]
			};

			myChart.setOption(option);
		}
	});
	
	setInterval(function () {
		$.ajax({
			type: "GET",
			async:true,
			url: php_url,
			data: {date:dt_str},
			dataType: "json",
			success: function(rs){
				option = {
					series: rs[0]
				};
	
				myChart.setOption(option);
			}
		});
	}, 2 * 60 * 1000);
};
