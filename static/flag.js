var flag_image_array = new Array();
var fav_image_array = new Array();
var region_code_array = new Array();
var duplicate = false;
var fav_index = 0;

// hardcode flags
flag_image_array[0] = new Image();
flag_image_array[0].src = '/static/resources/br.png';
region_code_array.push('br');
flag_image_array[1] = new Image();
flag_image_array[1].src = '/static/resources/ca.png';
region_code_array.push('ca');
flag_image_array[2] = new Image();
flag_image_array[2].src = '/static/resources/es.png';
region_code_array.push('es');
flag_image_array[3] = new Image();
flag_image_array[3].src = '/static/resources/fi.png';
region_code_array.push('fi');
flag_image_array[4] = new Image();
flag_image_array[4].src = '/static/resources/hu.png';
region_code_array.push('hu');
flag_image_array[5] = new Image();
flag_image_array[5].src = '/static/resources/id.png';
region_code_array.push('id');
flag_image_array[6] = new Image();
flag_image_array[6].src = '/static/resources/ie.png';
region_code_array.push('ie');
flag_image_array[7] = new Image();
flag_image_array[7].src = '/static/resources/it.png';
region_code_array.push('it');
flag_image_array[8] = new Image();
flag_image_array[8].src = '/static/resources/jp.png';
region_code_array.push('jp');
flag_image_array[9] = new Image();
flag_image_array[9].src = '/static/resources/kr.png';
region_code_array.push('kr');
flag_image_array[10] = new Image();
flag_image_array[10].src = '/static/resources/no.png';
region_code_array.push('no');
flag_image_array[11] = new Image();
flag_image_array[11].src = '/static/resources/np.png';
region_code_array.push('np');
flag_image_array[12] = new Image();
flag_image_array[12].src = '/static/resources/pe.png';
region_code_array.push('pe');
flag_image_array[13] = new Image();
flag_image_array[13].src = '/static/resources/ph.png';
region_code_array.push('ph');
flag_image_array[14] = new Image();
flag_image_array[14].src = '/static/resources/ru.png';
region_code_array.push('ru');
flag_image_array[15] = new Image();
flag_image_array[15].src = '/static/resources/se.png';
region_code_array.push('se');
flag_image_array[16] = new Image();
flag_image_array[16].src = '/static/resources/sg.png';
region_code_array.push('sg');
flag_image_array[17] = new Image();
flag_image_array[17].src = '/static/resources/ug.png';
region_code_array.push('ug');
flag_image_array[18] = new Image();
flag_image_array[18].src = '/static/resources/us.png';
region_code_array.push('us');
flag_image_array[19] = new Image();
flag_image_array[19].src = '/static/resources/vn.png';
region_code_array.push('vn');
flag_image_array[20] = new Image();
flag_image_array[20].src = '/static/resources/ye.png';
region_code_array.push('ye');

// display hardcoded flags
for (let i = 0; i <= 20; i++) {
    let temp = document.createElement('div');
    temp.className = 'item';
    temp.innerHTML = '<img src=' + flag_image_array[i].src + '><button onclick="add_to_fav(' + i + ')">FAV</button>';
    document.getElementById('container').appendChild(temp);
}
// Default: 21 flags displayed in the screen 

// function to add flag to fav_image_array, only if array length < 4
function add_to_fav(i) {
    duplicate = false;
    if (fav_index < 4) {
        // first input when there is no fav flags
        if (fav_index == 0) {
            let temp = document.createElement('div');
            temp.className = 'item';
            temp.innerHTML = '<img id="' + fav_index + '" src=' + flag_image_array[i].src + '>';
            document.getElementById('fav_container').appendChild(temp);
            fav_index++;
            fav_image_array.push(flag_image_array[i]);
        }

        let temp = document.createElement('div');
        temp.className = 'item';
        temp.innerHTML = '<img id="' + fav_index + '" src=' + flag_image_array[i].src + '>';

        // check duplicate flags
        for (let j = 0; j < fav_index; j++) {
            if (flag_image_array[i] == fav_image_array[j]) {
                duplicate = true;
            }
        }
        if (!duplicate) {
            document.getElementById('fav_container').appendChild(temp);
            fav_index++;
            fav_image_array.push(flag_image_array[i]);
        }
    }

    // when fav_index == 4 create 'save' button and personalize by user
    if (fav_index == 4) {

    }
}
