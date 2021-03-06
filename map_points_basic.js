queue() // javascript is asynchronous; queue runs the awaiting makeMap function only after the data files load
  .defer(d3.json, "https://gist.githubusercontent.com/blehman/60a7e05145bca836cb14/raw/45bdba3ec8eeaff862b38ee2e0affdf8c431ea09/world.json")
  .defer(d3.json, "twitterData.json")
  .await(makeMap);

function makeMap(error,world,geoData){
    var width = 960,
        height = 700;
    
    var projection = d3.geo.ginzburg5() 
        .scale(180) // total map size adjustment 
        .translate([width / 2, height / 2]) // map center 

    var path = d3.geo.path() // a function that essentially just draws lines
        .projection(projection); // translates the geo coords to screen coordinates
  
    var svg = d3.select("body").append("svg") // selections are arrays of dom elements
        .attr("width", width) 
        .attr("height", height)

    var feature = svg.append("path") // appends a path element to the svg
        .datum(topojson.feature(world, world.objects.land)) // accesses the land features and appends them to the path element
        .attr("d", path) // uses the path function to add directions for how to draw
        .attr("stroke","#000");  // adds the country outline

    var bounds = svg.insert("path")
      .datum(topojson.feature(world, world.objects.countries))
      .attr("class", "boundary")
      .attr("d", path)
      .attr("fill","#ccc");

    var large_circle = svg.selectAll(".bigPoints")
                   .data(geoData.features) // selects features to bind to the elements classed as points 
                   .enter() // binds the correct number of elements
                   .append("circle") // adds data bound circle elements to the graph
                   .style("stroke","steelblue")// overides the css to the color the circles
                   .classed("bigPoints",true)
                   .attr("cx",0)
                   .attr("cy",0)
                   .attr("transform", function(d){ return "translate("+path.centroid(d)+")"})// uses the path function to translate the long,lat into screen coords 
                   .attr("r",20) // sets the radius

    var small_circle = svg.selectAll(".points")
                   .data(geoData.features) // selects features to bind to the elements classed as points 
                   .enter() // binds the correct number of elements
                   .append("circle") // adds data bound circle elements to the graph
                   .classed("points",true) //  classes the circle elements
                   .attr("cx",0)
                   .attr("cy",0)
                   .attr("transform", function(d){ return "translate("+path.centroid(d)+")"})// uses the path function to translate the long,lat into screen coords 
                   .attr("r",2) // sets the radius

};