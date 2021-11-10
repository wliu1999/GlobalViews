var flag_image_array = new Array();

// create flag images using new Image()
flag_image_array[0] = new Image();
flag_image_array[0].src = '/static/resources/br.png';
flag_image_array[1] = new Image();
flag_image_array[1].src = '/static/resources/ca.png';
flag_image_array[2] = new Image();
flag_image_array[2].src = '/static/resources/es.png';
flag_image_array[3] = new Image();
flag_image_array[3].src = '/static/resources/fi.png';
flag_image_array[4] = new Image();
flag_image_array[4].src = '/static/resources/hu.png';
flag_image_array[5] = new Image();
flag_image_array[5].src = '/static/resources/id.png';
flag_image_array[6] = new Image();
flag_image_array[6].src = '/static/resources/ie.png';
flag_image_array[7] = new Image();
flag_image_array[7].src = '/static/resources/it.png';
flag_image_array[8] = new Image();
flag_image_array[8].src = '/static/resources/jp.png';
flag_image_array[9] = new Image();
flag_image_array[9].src = '/static/resources/kr.png';
flag_image_array[10] = new Image();
flag_image_array[10].src = '/static/resources/no.png';
flag_image_array[11] = new Image();
flag_image_array[11].src = '/static/resources/np.png';
flag_image_array[12] = new Image();
flag_image_array[12].src = '/static/resources/pe.png';
flag_image_array[13] = new Image();
flag_image_array[13].src = '/static/resources/ph.png';
flag_image_array[14] = new Image();
flag_image_array[14].src = '/static/resources/ru.png';
flag_image_array[15] = new Image();
flag_image_array[15].src = '/static/resources/se.png';
flag_image_array[16] = new Image();
flag_image_array[16].src = '/static/resources/sg.png';
flag_image_array[17] = new Image();
flag_image_array[17].src = '/static/resources/ug.png';
flag_image_array[18] = new Image();
flag_image_array[18].src = '/static/resources/us.png';
flag_image_array[19] = new Image();
flag_image_array[19].src = '/static/resources/vn.png';
flag_image_array[20] = new Image();
flag_image_array[20].src = '/static/resources/ye.png';

// method for displaying images
function display_image(flag_image_array) {
    for (let i = 0; i <= 20; i++) {
        let temp = document.createElement('div');
        temp.className = 'item';
        temp.innerHTML = '<img src=' + flag_image_array[i].src + '>';
        document.getElementById('container').appendChild(temp);
    }
}

display_image(flag_image_array);
