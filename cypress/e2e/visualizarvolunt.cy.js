describe('template-spec',()=> {
    it('teste visualizar voluntários', () =>{
        cy.visit('http://127.0.0.1:8000/visualizar_trabalheconosco/')
        cy.wait(2000)
        cy.scrollTo('bottom')
    })
})