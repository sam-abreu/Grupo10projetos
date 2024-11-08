describe('template spec', () =>{
    it('teste doar', () =>{
        cy.visit('http://127.0.0.1:8000/comprar/')
        cy.wait(1000)
        cy.get('#brinquedo').select('Carrinho - R$ 34.00')
        cy.wait(1000)
        cy.get('#quantidade').clear().type(3)
        cy.wait(1000)
        cy.get('#comprar-btn').click()
        cy.wait(10000)
    })

    it('teste doar NF', () =>{
        cy.visit('http://127.0.0.1:8000/comprar/')
        cy.wait(1000)
        cy.get('#brinquedo').select('Carrinho - R$ 34.00')
        cy.wait(1000)
        cy.get('#quantidade').clear()
        cy.wait(1000)
        cy.get('#comprar-btn').click()
        cy.wait(10000)
        //Esse tempo está maior pra que no screencast expliquemos essa história e seu funcionamento em específico
        //NÃO ESQUECER
    })
})