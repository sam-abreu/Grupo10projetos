describe('template spec', () =>{
    it('teste adicionar', () => {
        cy.visit('http://127.0.0.1:8000/add-brinquedo/')
        cy.wait(1000)
        cy.get(':nth-child(2) > input').type('Caminhão de plástico')
        cy.wait(1000)
        cy.get(':nth-child(3) > input').type(50)
        cy.wait(1000)
        cy.get(':nth-child(4) > input').type('3-8 Anos')
        cy.wait(1000)
        cy.get(':nth-child(5) > input').type('Plástico')
        cy.wait(1000)
        cy.get('button[type="submit"]').click({ force: true });
        cy.wait(1000)
    })

    it('teste adicionar NF', () =>{
        //Este código aqui se refere a um teste não funcional
        cy.visit('http://127.0.0.1:8000/add-brinquedo/')
        cy.wait(1000)
        cy.get(':nth-child(2) > input').type('Caminhão de plástico')
        cy.wait(1000)
        cy.get(':nth-child(3) > input').type('R$50,00')
        cy.wait(1000)
        cy.get(':nth-child(4) > input').type('3-8 Anos')
        cy.wait(1000)
        cy.get(':nth-child(5) > input').type('Plástico')
        cy.wait(1000)
        cy.get('button[type="submit"]').click({ force: true });
        cy.wait(1000)
    })
})