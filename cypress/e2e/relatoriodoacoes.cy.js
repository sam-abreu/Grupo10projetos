describe('template spec',() =>{

    it('teste relatorio', () =>{
        cy.visit('http://127.0.0.1:8000/adminpage/')
        cy.wait(2000)
        cy.get('.excel-button').click({force : true})
        cy.wait(3000)
    })
})