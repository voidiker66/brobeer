  function iterateThroughGitlab(parameters, results_per_page, page_number, check) {
    var temp_url = parameters.url;
    var headers = "";

    parameters.url += "?per_page=" + results_per_page + "&page=" + page_number;
    $.ajax(parameters).done(function(response, textStatus, xhr) {
        getResponses(response, check);
        headers = xhr.getAllResponseHeaders();
        var arr = headers.trim().split(/[\r\n]+/);

        // Create a map of header names to values
        var headerMap = {};
        arr.forEach(function (line) {
          var parts = line.split(': ');
          var header = parts.shift();
          var value = parts.join(': ');
          headerMap[header] = value;
        });
        var pages = headerMap["X-Total-Pages"];
        for (var y = 2; y <= pages; y++) {
          parameters.url = temp_url + "?per_page=" + results_per_page + "&page=" + y;
          $.ajax(parameters).done(function(response, textStatus, xhr) {
            getResponses(response, check);
        });
        }
      });
}

  function incrementThings(name, check) {
      var div = "#" + name + "-" + check;
      $(div)[0].innerHTML = parseInt($(div)[0].innerHTML) + 1;
      $("#total_" + check + "s")[0].innerHTML = parseInt($("#total_" + check + "s")[0].innerHTML) + 1;
  }

  function getResponses(response, check) {
      for (var x in response) {
            var name = response[x].author_name ? response[x].author_name : response[x].author.name;
            var user = "";
          if (name === "Victor Chau") {
            user = "victor";
          }
          else if (name === "Austin Ikerd" || name === "voidiker66" || name === "AustinIkerd") {
            user = "austin";
          }
          else if (name === "joseph bess" || name === "Joseph Bess") {
            user = "joseph";
          }
          else if (name === "kamran629" || name === "Kamran A Khan") {
            user = "kamran";
          }
          else if (name === "sean_yi" || name === "Sean Yi") {
            user = "sean";
          }
          else {
            console.log(name + " not yet config");
            continue;
          }
          incrementThings(user, check)
        }
    }

var parameters = {
    url: "https://gitlab.com/api/v4/projects/7229879/repository/commits",
    async: true,
    crossDomain: true,
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    method: "GET",
    mozSystem: true
  };
  iterateThroughGitlab(parameters, 100, 1, "commit");

  var parameters2 = {
    url: "https://gitlab.com/api/v4/projects/7229879/issues",
    async: true,
    crossDomain: true,
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    method: "GET",
    mozSystem: true
  };
  iterateThroughGitlab(parameters2, 100, 1, "issue");