function drawChart(chartname, charttitle, php_name='', type='') {
	var myChart = echarts.init(document.getElementById(chartname));
	if (php_name == '')
		php_name = chartname;
	var php_url = "php/" + php_name + ".php";

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
	var legend = [];
	var series = [];

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
            y:45,
            x2:20,
            y2:20
        },		
		color: ['#66d', '#6d6', '#d66', '#6dd', '#d6d', '#dd6', '#d96'],
		backgroundColor: '#000',
		legend: {
			right: '1%',
			width: '100%',
			top: '7%',
			formatter: name,
			itemWidth: 14,
			itemHeight: 7,
			textStyle: {
				fontSize: 9,
				color:'#ddd'
			},
			borderWidth: 0,
			orient: 'horizontal' 
		},
		tooltip: {
			trigger: 'axis',
			textStyle: {
				fontSize: 9
			},
			axisPointer: {
				animation: false
			}
		},
		xAxis: {
			type: 'time',
			//type: 'category',
			axisLine:{
				lineStyle: {
					color:'#ddd',
					width: 2
				}
			},
			axisTick:{
				show: false
			},
			axisLabel:{
				show: false,
				textStyle: {
					fontSize: 8,
					color:'#ddd'
				}
			},
			splitLine: {
				show: false
			}
		},
		yAxis: [{
			type: 'value',
			max: 'dataMax',
			show: false,
			//min: 'dataMin',
			//boundaryGap: [0, '100%'],
			axisLine:{
				//onZero: false,
				lineStyle: {
					color:'#ddd',
					width: 2
				}
			},
			axisTick:{
				show: false
			},
			axisLabel:{
				show: false,
				textStyle: {
					color:'#ddd'
				}
			},
			splitLine: {
				show: false
			},
		},
		{
			type: 'value',
			show: false,
			//max: 'dataMax',
			//min: 'dataMin',
			boundaryGap: [0, '100%'],
			axisLine:{
				lineStyle: {
					color:'#ddd',
					width: 2
				}
			},
			axisTick:{
				show: false
			},
			axisLabel:{
				show: false,
				textStyle: {
					color:'#ddd'
				}
			},
			splitLine: {
				show: false
			},
		}],
	};

	myChart.setOption(option);

	$.ajax({
		type: "GET",
		async: true,
		url: php_url,
		data: {date:dt_str, type:type},
		dataType: "json",
		success: function(rs){
			legend = rs[0];
			//alert(legend);
			series = rs[1];
			//series.forEach(function(value, index, array){
				//value.symbolSize = 4;
				//value.areaStyle = "{normal: {}}";
			//})
			option = {
				legend: {
					data:legend
				},
				series: series
			};
			myChart.setOption(option);
		}
	});
};
