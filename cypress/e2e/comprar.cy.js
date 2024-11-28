describe('template spec', () =>{
    it('teste doar', () =>{
        cy.visit('http://127.0.0.1:8000/')
        cy.wait(1000)
        cy.get('#username').type("Mario")
        cy.wait(1000)
        cy.get('#password').type("yoshi")
        cy.wait(1000)
        cy.get('button').click()
        cy.wait(1000)
        cy.visit('http://127.0.0.1:8000/comprar/')
        cy.wait(1000)
        cy.get('#quantidade').clear().type(3)
        cy.wait(1000)
        cy.get('#comprar-btn').click()
        cy.wait(7000)
    })

    it('teste doar NF', () =>{
        cy.visit('http://127.0.0.1:8000/')
        cy.wait(1000)
        cy.get('#username').type("Mario")
        cy.wait(1000)
        cy.get('#password').type("yoshi")
        cy.wait(1000)
        cy.get('button').click()
        cy.wait(1000)
        cy.visit('http://127.0.0.1:8000/comprar/')
        cy.wait(1000)

        cy.get('#quantidade').clear()
        cy.wait(1000)
        cy.get('#comprar-btn').click()
        cy.wait(4000)
        //Segundo teste nao funciona pq o espaço quantidade nao esta preenchido
        //Esse tempo está maior pra que no screencast expliquemos essa história e seu funcionamento em específico
        //NÃO ESQUECER
    })
})