app={ 
	init:function(){
		if(! window.localStorage){     
			return false;
		}  
		key = localStorage.getItem("key") || prompt("输入你的id");
		localStorage.setItem("key",key);

		map.centerAndZoom("济南",12);                
		map.enableScrollWheelZoom();   //启用滚轮放大缩小，默认禁用
		map.enableContinuousZoom();    //启用地图惯性拖拽，默认禁用
		map.setDefaultCursor("url('bird.cur')");//设置鼠标样式


		$(".myimg").click(this.click);
		$("#iwantsay").change(this.change);
		this.on();
		setInterval(function(){
			app.gps();
		},3000);
		
	},
	gps:function(){
		var geolocation = new BMap.Geolocation();
		//通过浏览器获取经纬度
		geolocation.getCurrentPosition( this.callbackgps ,{enableHighAccuracy: true});
	},
	callbackgps:function(r){ 
		mypoint=r.point; 
	},
	click:function(){
		var container=$(".myContainer");
		var myimg=$(".myimg");
		var toggle=$(".toggle");
		if(container.css("bottom")=="10px"){
			container.animate({bottom:"-1000px"},"slow");
			toggle.show();
		}else{
			container.animate({bottom:"10px"},"slow");
			toggle.hide();
		}

	},
	change:function(){
		var iwantsay=$("#iwantsay").val();
		localStorage.setItem("iwantsay",iwantsay); 
		var data={
			"lng":mypoint.lng,
			"lat":mypoint.lat,
			"key":key,
			"msg":iwantsay,
		}; 
		Wdog.child(key).set(data);
	},
	addmark:function(item){

		var mk = new BMap.Marker({"lng":item.lng,"lat":item.lat});
		map.addOverlay(mk);
		map.panTo({"lng":item.lng,"lat":item.lat});  
		var point = new BMap.Point(item.lng,item.lat);
		var marker = new BMap.Marker(point);  // 创建标注
		map.addOverlay(marker);              // 将标注添加到地图中   
		var opts = {
		  width : 200,     // 信息窗口宽度
		  height: 100,     // 信息窗口高度
		  title : "Message" , // 信息窗口标题
		}
		var infoWindow = new BMap.InfoWindow(item.msg, opts);  // 创建信息窗口对象 
		marker.addEventListener("click", function(){          
			map.openInfoWindow(infoWindow,point); //开启信息窗口
		});
	},
	on:function(){
		 
		Wdog.on("value", function(datasnapshot) {  
		     var points=datasnapshot.val();
		     $.each(points,function(k,item){ 
	     		app.addmark(item);
		     }) 
		}, function(error){
		    // 处理请求失败打错误
		    console.log("网络错误");
		});
		 
	}

};

$(function(){
	today=new Date();  
	year=today.getFullYear().toString();
	month=(today.getMonth()+1).toString();
	day=today.getDate().toString();
	today=year+"/"+month+"/"+day;
	map = new BMap.Map("allmap");
	Wdog = new Wilddog("https://poke.wilddogio.com/"+today);
	mypoint={lng:null,lat:null,};
	app.init(map);	 
});
