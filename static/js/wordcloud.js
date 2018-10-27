function word_cloud(cloud) {  
    var option = {  
        tooltip : {},  
        series : [ {  
            type : 'wordCloud',  
            shape:'smooth',  
            //shape: 'ellipse',
            gridSize : 10,  
            sizeRange : [ 10, 24 ],  
            rotationRange : [ 0, 0 ],  
            textStyle: {
                normal: {
                    fontFamily: '微软雅黑',
                    color: function () {
                        //var colors = ['#fda67e', '#81cacc', '#cca8ba', "#88cc81", "#82a0c5", '#fddb7e', '#735ba1', '#bda29a', '#6e7074', '#546570', '#c4ccd3'];
                        var colors = ['#66d', '#6d6', '#d66', '#6dd', '#d6d', '#dd6', '#d96'];
                        return colors[parseInt(Math.random() * 7)];
                    }
                }
            },
            data : cloud  
        } ]  
    };  
    return option;  
}  

function drawCloud(chartname, charttitle, flask_path='', type='') {
	var myChart = echarts.init(document.getElementById(chartname));
	if (flask_path == '')
		flask_path = chartname;
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

	var cloud_data=[{name: 'Sam S Club',value: 10000}, {name: 'Macys',value: 6181},{name: 'Amy Schumer',value: 4386},{name: 'Jurassic World',value: 4055},{name: 'Charter Communications',value: 2467},{name: 'Chick Fil A',value: 2244},{name: 'Planet Fitness',value: 1898},{name: 'Pitch Perfect',value: 1484},{name: 'Express',value: 1112},{name: 'Home',value: 965},{name: 'Johnny Depp',value: 847},{name: 'Lena Dunham',value: 582},{name: 'Lewis Hamilton',value: 555},{name: 'KXAN',value: 550},{name: 'Mary Ellen Mark',value: 462},{name: 'Farrah Abraham',value: 366},{name: 'Rita Ora',value: 360},{name: 'Serena Williams',value: 282},{name: 'NCAA baseball tournament',value: 273},{name: 'Point' ,value: 273},{name: 'Point Break',value: 265}];
	var option = word_cloud(cloud_data);

	myChart.setOption(option);

	$.ajax({
		type: "GET",
		async: true,
		url: flask_path,
		data: {date:dt_str, type:type},
		dataType: "json",
		success: function(rs){
			legend = rs[0];
			//alert(legend);
			series = rs[1];
			xAxis = rs[2];
			//series.forEach(function(value, index, array){
				//value.symbolSize = 4;
				//value.areaStyle = "{normal: {}}";
			//})
			option = {
				xAxis: {
					data:xAxis
				},
				legend: {
					data:legend
				},
				series: series
			};
			//myChart.setOption(option);
		}
	});
};
