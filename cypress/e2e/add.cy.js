describe('template spec', () =>{
    it('teste adicionar', () => {
        cy.visit('http://127.0.0.1:8000/add-brinquedo/')
        cy.wait(1000)
        cy.get('#nome').type('Caminhão de plástico', {force : true})
        cy.wait(1000)
        cy.get('#preco').type(50)
        cy.wait(1000)
        cy.get('#faixaetaria').type('3-8 Anos', {force : true})
        cy.wait(1000)
        cy.get('#material').type('Plástico')
        cy.wait(1000)
        Cypress.on('uncaught:exception', (err, runnable) => {
            console.error('Erro detectado:', err);
            return false; 
          });
        cy.get('.btn').click({force : true});
        cy.wait(2000)
    })

    it('teste adicionar NF', () =>{
        //Este código aqui se refere a um teste não funcional
        cy.visit('http://127.0.0.1:8000/add-brinquedo/')
        cy.wait(1000)
        cy.get('#nome').type('Caminhão de plástico', {force : true})
        cy.wait(1000)
        cy.get('#preco').type('50 R$')
        cy.wait(1000)
        cy.get('#faixaetaria').type('3-8 Anos', {force : true})
        cy.wait(1000)
        cy.get('#material').type('Plástico')
        cy.wait(1000)
        cy.get('.btn').click({ force: true });
        cy.wait(1000)
    })
})