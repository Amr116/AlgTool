    /* Functions to assign ID's to dropped building blocks*/

    String.prototype.replaceAll = function (find, replace) {
        var str = this;
        return str.replace(new RegExp(find.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&'), 'g'), replace);
    };

    var idCounter = 0;
    var allIDs = [];
    function giveID(caller){
        idCounter++;
        allIDs.push(caller+idCounter);
        console.log(caller+idCounter);
        return caller + idCounter;
    }
    function assignID(id,str){
        str = str.toLowerCase();
        id = id.toLowerCase();
        //str = str.replaceAll(/id="/+id+/"/gi, ('id="'+ giveID(id)+ '"'));
        //str = str.split('id="'+id+'"').join('id="'+ giveID(id)+ '"');
        while (str.search('id="'+id+'"') != -1){
            len1 = str.length;
            len = str.substring(0,str.search('id="'+id+'"')).length+('id="'+id+'"').length;
            str = str.substring(0,str.search('id="'+id+'"')) + ('id="'+ giveID(id)+ '"') + str.substring(len, len1);
        }

        console.log(str);
        return str;
    }

    /* */

    function test() {
        var test= document.getElementById("my-textarea").innerHTML;
        alert(test);
    }

    function allowDrop(ev) {
        ev.preventDefault();
    }

    function drag(event) {
        event.dataTransfer.setData("text", event.target.id);
    }

    var LineId = 1;

    function dropLines(ev) {
        ev.preventDefault();

        var test = ev.target.tagName;
        if (test == "LI"){
            var id = ev.dataTransfer.getData("text");
            var str = '<li>' + insert(id) + '</li>';
            str = assignID(id, str);
            var child = document.createElement('div');
            child.innerHTML = str;
            child = child.firstChild;

            ev.target.parentNode.appendChild(child);
            ev.stopPropagation();
            saveData(id);

            LineId += 1;
            return false;
        }
        else{
            var id = ev.dataTransfer.getData("text");
            var str = '<li>' + insert(id) + '</li>';
            str = assignID(id, str);
            var child = document.createElement('div');
            child.innerHTML = str;
            child = child.firstChild;

            ev.target.appendChild(child);
            ev.stopPropagation();
            saveData(id);

            LineId += 1;
            return false;
        }
    }

    function drop(ev) {
        ev.preventDefault();

        if (ev.target.hasChildNodes()){
            ev.stopPropagation();
        }

        else{
            var id = ev.dataTransfer.getData("text");
            console.log(id);
            var str = insert(id);
            str = assignID(id, str);
            var child = document.createElement('div');
            child.innerHTML = str;
            child = child.firstChild;

            ev.target.appendChild(child);
            ev.stopPropagation();
            saveData(id);
            return false;
        }
    }

    var i = 1;
    function saveData(LineId,id) {
        //var obj = [];

        obj = {LineId, id};
        localStorage.setItem('myStorage', JSON.stringify(obj));
        //i += 1;
    }
    function getdata() {
        var data = JSON.parse(localStorage.getItem('myStorage'));
        //document.getElementById("result").innerHTML = "key is "+data.i;
        document.getElementById("result").innerHTML = "key is"+data.LineId+"<br>value is "+data.id+"<br>";

        //for(var count = 0; count < 10; count ++) {
        //    localStorage.getItem('myStorage').length;
        //}

    //    var data = JSON.parse(localStorage.getItem('myStorage'));
    //    document.getElementById("result").innerHTML = data;
    }
    function cleanStoarge() {
        localStorage.clear();
        document.getElementById("result").innerHTML = "you have cleared data";
    }

    function readLine() {
        var line = document.getElementById("my-textarea").children[0];
        console.log(line);
        var print_result = evaluate(line);
        document.getElementById("print_result").innerHTML = 'result is ' + print_result;
    }
    
    