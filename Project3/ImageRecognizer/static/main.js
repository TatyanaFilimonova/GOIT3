let currentDirectionIndex;

function onLoadDirection() {
  currentDirection = document.getElementById('direction');
  currentDirectionIndex = currentDirection.selectedIndex;
  console.log(currentDirection.options[currentDirectionIndex]);
};


function submitForm(formName){
    if (validFormData(formName)){
        document.getElementById(formName).submit()
    }
}


function clearHistory(event){
    event.preventDefault();
    console.log('try preventDefault')
    window.location.href = '/IR/ch/';
}

function validFormData(formName) {
    const form = document.forms[formName];
    const formData = new FormData(form);
    const keys = formData.keys();
    for (const key of keys) {
        if (!form[key].validity.valid) {
                form[key].focus();
                return false;
        }
    }
    return true;
}

function closeDirectionModal(modalId){
    console.log(currentDirectionIndex);
    currentDirection = document.getElementById(modalId);
    document.getElementById('direction').options[currentDirectionIndex].selected = true;
    currentDirection.style.display = 'none';
}



