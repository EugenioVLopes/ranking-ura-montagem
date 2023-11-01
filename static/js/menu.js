function menuModal(selecionado){
    
    //botoes
    let btn_cadastro = document.getElementById('btn-cadastrar');
    let btn_participantes = document.getElementById('btn-participantes');

    //divs
    let visualizacao_cadastro = document.getElementById('div-cadastro');
    let visualizacao_participantes = document.getElementById('div-participantes');
    
    if(selecionado == 'cadastro'){

        //Mudando botão de cadastro para "selecionado"
        btn_cadastro.classList.remove('btn-outline-primary');
        btn_cadastro.classList.add('btn-primary')

        //Mudando botão de participantes para "não selecionado"
        btn_participantes.classList.add('btn-outline-primary');
        btn_participantes.classList.remove('btn-primary');
        
        //Mudando a visualização para div clicada
        visualizacao_cadastro.classList.remove('hide');
        visualizacao_participantes.classList.add('hide');

    }else{

        //Fazendo a situação invers

        btn_cadastro.classList.add('btn-outline-primary');
        btn_cadastro.classList.remove('btn-primary')

        //Mudando botão de participantes para "não selecionado"
        btn_participantes.classList.remove('btn-outline-primary');
        btn_participantes.classList.add('btn-primary');
        
        //Mudando a visualização para div clicada
        visualizacao_cadastro.classList.add('hide');
        visualizacao_participantes.classList.remove('hide');
    }
}