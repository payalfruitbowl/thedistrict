import os

file_path = "three_scene.js"

with open(file_path, "r") as f:
    content = f.read()

# Replace the GSAP animation for #ai to include a timeline with multiple steps
old_gsap = """        // 1. AI Section: Move to the right and scale down
        gsap.to(target.position, {
            x: 2.5,
            y: 0.5,
            z: -2,
            ease: "power2.inOut",
            scrollTrigger: {
                trigger: "#ai",
                start: "top 80%",
                end: "center center",
                scrub: 1
            }
        });
        gsap.to(target.rotation, {
            x: Math.PI / 2,
            y: Math.PI,
            ease: "power2.inOut",
            scrollTrigger: {
                trigger: "#ai",
                start: "top 80%",
                end: "center center",
                scrub: 1
            }
        });"""

new_gsap = """        // 1. AI Section: Timeline for multiple scrolls
        const aiTl = gsap.timeline({
            scrollTrigger: {
                trigger: "#ai",
                start: "top 80%",
                end: "center center",
                scrub: 1
            }
        });
        
        // Step 1: Move to right (2nd scroll)
        aiTl.to(target.position, {
            x: 2.5,
            y: 0.5,
            z: -2,
            duration: 1,
            ease: "power2.inOut"
        }, 0);
        aiTl.to(target.rotation, {
            x: Math.PI / 2,
            y: Math.PI,
            duration: 1,
            ease: "power2.inOut"
        }, 0);

        // Step 2: Move back to center and scale up (3rd scroll)
        aiTl.to(target.position, {
            x: 0,
            y: -0.5,
            z: 2,
            duration: 1.5,
            ease: "power2.inOut"
        }, 1.5);
        aiTl.to(target.rotation, {
            x: Math.PI / 4,
            y: Math.PI * 2,
            z: 0,
            duration: 1.5,
            ease: "power2.inOut"
        }, 1.5);"""

content = content.replace(old_gsap, new_gsap)

with open(file_path, "w") as f:
    f.write(content)

print("Updated three_scene.js")
