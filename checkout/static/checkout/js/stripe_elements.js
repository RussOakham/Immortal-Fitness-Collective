/*
    Core Logic/payment flow and CSS comes from:
    https://stripe.com/docs/libraries
*/

var stripe_public_key = $("#id_stripe_public_key").text().slice(1, -1);
var client_secret = $("#id_client_secret").text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
  base: {
    color: "var(--colour-black)",
    "::placeholder": {
      color: "#aab7c4",
    },
  },
  invalid: {
    color: "var(--colour-red)",
    iconColor: "var(--colour-red)",
  },
};

var card = elements.create("card", { style: style });
card.mount("#checkout__card-element");