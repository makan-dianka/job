btn = document.querySelector('.research-btn')
spinner = document.querySelector('.sp')

btn.addEventListener('click', function(){
    inp = document.querySelector('#research')
    if (inp.value){
        spinner.classList.remove('sp')

        sleep(100).then(() => {
            btn.disabled=true
        });
    }

})


function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
  }