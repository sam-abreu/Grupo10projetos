describe('template spec', () =>{
    it('teste visualizar doações', () =>{
        cy.visit('http://127.0.0.1:8000/visualizar_doacao/')
        cy.wait(2000)
        cy.scrollTo('bottom')
        cy.wait(2000)
    })
})