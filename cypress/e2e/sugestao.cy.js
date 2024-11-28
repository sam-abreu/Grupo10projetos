describe('template spec', () =>{
    it('teste sugestao', () => {
        cy.visit('http://127.0.0.1:8000/sugestao_brinquedo')
        cy.wait(1000)
        cy.get('#idade').type(2)
        cy.wait(1000)
        cy.get('#sexo').select('Masculino')
        cy.wait(1000)
        cy.get('.btn').click()
        cy.wait(3000)
    })
 
    it('teste sugestao NF', () =>{
        cy.visit('http://127.0.0.1:8000/sugestao_brinquedo')
        cy.wait(1000)
        cy.get('#idade').type(300)
        cy.wait(1000)
        cy.get('#sexo').select('Masculino')
        cy.wait(1000)
        cy.get('.btn').click()
        cy.wait(3000)
    })
})