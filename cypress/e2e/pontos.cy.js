describe('temlpate-spec', () =>{
    it('teste pontos', () => {
        cy.visit('http://127.0.0.1:8000/')
        cy.wait(1000)
        cy.get('#username').type("Mario", {force : true})
        cy.wait(1000)
        cy.get('#password').type("yoshi", {force : true})
        cy.get('button').click({force : true})
        cy.wait(3000)          
        Cypress.on('uncaught:exception', (err, runnable) => {
            console.error('Erro detectado:', err);
            return false; 
          });
        cy.get('#userButton').click();
        cy.wait(1000)
        cy.get('#closeSidebar').click({force : true});
        cy.wait(3000)
    })
})