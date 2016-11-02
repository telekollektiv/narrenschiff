window.onload = (function() {
    var form = document.getElementById('instruction-form');
    var txt = document.getElementById('input-txt');
    var apiResponse = document.getElementById('api-response');

    form.onsubmit = function(e) {
        e.preventDefault();

        if(!txt.value) return;

        var data = new FormData();
        data.append('txt', txt.value);

        fetch('/send', {
            method: 'post',
            body: data,
        })
        .then(r => r.json())
        .then(rep => {
            if(rep.status == 'success') {
                apiResponse.textContent = 'gesendet.';
            } else {
                apiResponse.textContent = 'zu viele Aufgaben, warte ein wenig :)';
            }
        });
    };
})();
