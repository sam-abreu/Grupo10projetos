describe('template spec', () =>{
    it('teste residuos', () =>{
        cy.visit('http://127.0.0.1:8000/residuos/')
        cy.wait(4000)
        cy.get('a').click()
        cy.wait(2000)
    })
})