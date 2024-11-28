describe('template spec', () =>{
    it('teste trabalhe_conosco', () =>{
        cy.visit('http://127.0.0.1:8000/trabalhe-conosco/')
        cy.wait(2000)
        cy.get('#nome').type('Alexander barbosa', {force : true});
        cy.wait(2000)
        cy.get('#email').type('alexanderbarbosa@gmail.com', {force : true})
        cy.wait(2000)
        cy.get('#telefone').type('(81) 99999-9999')
        cy.wait(2000)
        cy.get('#mensagem').type('Estou muito interessado em trabalhar com vocês e desejo contribuir com tudo que estiver ao meu alcance', {force : true})
        cy.get(6000)
        cy.get('button').click({force : true})
        cy.get(4000)
        

    })
})